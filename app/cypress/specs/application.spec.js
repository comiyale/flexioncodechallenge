/* eslint-disable no-undef */
describe("Loading the application", function() {
	it("The application should be reachable", function() {
		cy.visit("/");
	});
});

describe("Application Form test", () => {
	beforeEach(() => {
		cy.visit("/");
	});

	it("Should load the form", () => {
		cy.get("form");
	});

	it("Should fill in the question", () => {
		cy.get('input[name="question"]')
			.type("34.2")
			.should("have.value", "34.2");
	});

	it("Should be able to clear the question field", () => {
		cy.get('input[name="question"]').clear();
	});

	it("Should select a unit type to convert from", () => {
		cy.get('select[name="initial_unit"]')
			.select("Kelvin")
			.should("have.value", "Kelvin");
	});

	it("Should select a unit type to convert to", () => {
		cy.get('select[name="desired_unit"]')
			.select("Celsius")
			.should("have.value", "Celsius");
	});

	it("Should fill in the student answer", () => {
		cy.get('input[name="answer"]')
			.type("-134.2")
			.should("have.value", "-134.2");
	});

	it("Should be able to clear the student answer", () => {
		cy.get('input[name="answer"]').clear();
	});

	it("Should be able to display the result on the textarea", () => {
		cy.get("textarea")
			.type("correct", { force: true })
			.should("have.value", "correct");
	});

	it("Form should be able to submit", () => {
		cy.get("form").submit();
	});
});

describe("Testing the application API request", function() {
	it("Should be able to load unit types from the server", function() {
		cy.server();
		cy.route({
			url: `/api/get_units/`,
			method: "GET",
			status: 200,
		});
	});

	it("Should be able to post request to the server", function() {
		cy.server();
		cy.route("POST", "/api/convert/", {
			value: "84.2",
			student_response: "543.94",
			initial_unit: "Kelvin",
			desired_unit: "liters",
		});
	});
});
