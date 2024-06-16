describe('Prueba de integración de login', () => {
  it('Iniciar sesión desde Vue.js y verificar comunicación con Django', () => {
    // Visita la URL del frontend Vue.js
    cy.visit('http://localhost:8080/login/')  // Ajusta la URL según corresponda a tu entorno de desarrollo

    // Simula el inicio de sesión desde Vue.js
    cy.get('#usernameInput').type('test_user')  // Ajusta el selector según tu implementación de Vue.js
    cy.get('#passwordInput').type('test_password')  // Ajusta el selector según tu implementación de Vue.js
    cy.get('#login-form').submit();  // Ajusta el selector según tu implementación de Vue.js

    // Verifica que la comunicación con Django sea exitosa
    cy.request({
      method: 'POST',
      url: 'http://localhost:8000/login/',  // Ajusta la URL del endpoint de login en Django según corresponda
      body: {
        username: 'test_user',
        password: 'test_password'
      }
    }).then((response) => {
      expect(response.status).to.eq(200)
      // Agregar más aserciones según sea necesario para verificar la respuesta del backend
    })
  })
})