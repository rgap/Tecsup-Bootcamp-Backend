/* eslint-disable no-undef */
describe("template spec", () => {
  it("passes", () => {
    // cy.visit("https://example.cypress.io");
    cy.visit("http://localhost:3000/");
    cy.get("input[name='name']").type("linder");
    cy.get("input[name='lastname']").type("linder");
    cy.get("input[name='email']").type("linder@gmail.com");
    cy.get("input[name='password']").type("password");
  });
});
