<template>
	<div id="app" class="d-flex justify-content-center">
		<div class="contentWrapper">
			<div class="logoWrapper">
				<div class="circle">
					<span>UC</span>
				</div>
				<h4>Unit Converter</h4>
				<div class="line"></div>
				<p>
					Welcome to unit converter app to help
					<br />grade the scores of your students
				</p>
			</div>

			<div class="formBox">
				<form @submit.prevent="handleSubmit">
					<div class="form-group">
						<label>Question</label>
						<input
							v-model="question"
							class="form-control"
							name="question"
							type="text"
							placeholder="Input Numerical Value"
							@keyup="inputValidator('question')"
							id="question"
							required
						/>
						<small class="error" v-show="validation.question !== ''">
							{{ validation.question }}
						</small>
					</div>
					<div class="row">
						<div class="col">
							<div class="form-group">
								<label>Unit from</label>
								<select
									class="form-control"
									name="initial_unit"
									v-model="initial_unit"
									id="initial_unit"
									required
								>
									<option value disabled>--select unit--</option>
									<option
										v-for="(unit, index) in types"
										v-bind:key="index"
										:value="unit"
										>{{ unit }}</option
									>
								</select>
							</div>
						</div>
						<div class="col">
							<div class="form-group">
								<label>Unit To</label>
								<select
									class="form-control"
									name="desired_unit"
									v-model="desired_unit"
									id="desired_unit"
									required
								>
									<option value disabled>--select unit--</option>
									<option
										v-for="(unit, index) in types"
										v-bind:key="index"
										:value="unit"
										>{{ unit }}</option
									>
								</select>
							</div>
						</div>
					</div>
					<div class="form-group">
						<label>Student answer</label>
						<input
							v-model="answer"
							class="form-control"
							name="answer"
							type="text"
							placeholder="Student Response"
							@keyup="inputValidator('answer')"
							id="answer"
							required
						/>
						<small class="error" v-show="validation.answer !== ''">
							{{ validation.answer }}
						</small>
					</div>
					<div class="form-group">
						<label>Output</label>
						<textarea
							:class="
								`form-control ${
									result === 'incorrect' || result === 'invalid'
										? 'error'
										: 'correct'
								}`
							"
							v-model="result"
							readonly
						/>
					</div>
					<div class="d-flex justify-content-center">
						<button type="submit" class="btn btn-primary" :disabled="loading">
							Submit
						</button>
						<button type="reset" class="btn btn-default">Cancel</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
import { getUnitTypes, createConversion } from "../service";
export default {
	name: "App",
	data() {
		return {
			question: "",
			answer: "",
			initial_unit: "",
			desired_unit: "",
			error: null,
			loading: false,
			types: [],
			result: "",
			validation: {
				question: "",
				answer: "",
			},
		};
	},
	async created() {
		const values = [];
		const types = await getUnitTypes();
		const units = values.concat(types[0].temperature).concat(types[1].volume);
		this.types = units;
	},
	methods: {
		async handleSubmit(e) {
			e.preventDefault();
			this.loading = true;
			this.result = "";

			try {
				const payload = {
					value: this.question,
					initial_unit: this.initial_unit,
					desired_unit: this.desired_unit,
					student_response: this.answer,
				};

				const response = await createConversion(payload);
				this.result = response.data;
			} catch (err) {
				this.error = err.message;
			} finally {
				this.loading = false;
			}
		},
		inputValidator(field) {
			let value = field === "question" ? this.question : this.answer;
			if (new RegExp(/^-?(\d+\.?\d*|\d*\.?\d+)$/gm).test(value)) {
				if (field === "question") {
					this.validation.question = "";
					this.question = value;
				} else {
					this.validation.answer = "";
					this.answer = value;
				}
			} else {
				const error = "Invalid input! Only numeric values are allowed";
				if (field === "question") {
					this.validation.question = error;
				} else {
					this.validation.answer = error;
				}
			}
		},
	},
};
</script>
