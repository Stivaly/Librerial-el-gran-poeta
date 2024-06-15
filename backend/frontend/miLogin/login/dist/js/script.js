new Vue({
    el:".fondo",
    data:{
        form:{username:"",password:""}
    },
    mounted() {
        this.usernameInput = document.querySelector('input[name="{{ form.username.name }}"]');
        this.passwordInput = document.querySelector('input[name="{{ form.password.name }}"]');
        this.usernameInput.addEventListener('input', e => {
            this.form.username = e.target.value;
        });
        this.passwordInput.addEventListener('input', e => {
            this.form.password = e.target.value;
        });
    },
    methods:{
        enviarFormulario(){
            console.log(this.form)
        }
    },
    computed:{
        validarEmail(){
            var exp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            return !exp.test(this.form.username);
        },
        validarPassword(){
            var exp = /^(?=.*\d)(?=.*[a-záéíóúñ]).*[A-ZÁÉÍÓÚÜÑ]/;
            return !exp.test(this.form.password);
        }
    },
    watch: {
        'form.username': function(newVal, oldVal) {
            if (this.validarEmail) {
                this.usernameInput.classList.add('error');
            } else {
                this.usernameInput.classList.remove('error');
            }
        },
        'form.password': function(newVal, oldVal) {
            if (this.validarPassword) {
                this.passwordInput.classList.add('error');
            } else {
                this.passwordInput.classList.remove('error');
            }
        }
    }
})

