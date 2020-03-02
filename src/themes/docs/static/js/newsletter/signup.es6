/** @jsx h */

'use strict';

const { Component, h, render } = window.preact;

/** Example classful component */
class App extends Component {
    componentDidMount() {
        this.setState({ message:'Hello!' });
    }
    render(props, state) {
        return (
            h('div', {id:'app'},
                h(Form)
            )
        );
    }
}

var translations = {
    'Invalid email address.' : 'Bitte geben Sie eine gültige E-Mail Adresse an.'
}

/** Instead of JSX, use: h(type, props, ...children) */
class Form extends Component {

    state = {
        submitting : false,
        status: 'pending', 
        data : {
/*            name : 'Max Mustermann',
            email : 'max.mustermann@muster-ag.de',
            company : 'Muster AG',
            phone : '0324234234234'*/
        },
        errors: {}
    }

    encodeData(obj) {
        var str = []
        for(var p in obj)
            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]))
        return str.join("&")
    }

    submitData(data){
        
        var xhr = new XMLHttpRequest()
        var encodedData = this.encodeData(data)
        $.ajax({
            type: 'POST',
            url: "https://auth.kiprotect.com/api/newsletter/v1/subscribe/newsletter",
            crossDomain: true,
            data: encodedData,
        }).done(function(data){
            this.setState({status: 'success'})
        }.bind(this)).fail(function(xhr){
            var json = xhr.responseJSON
            if (json !== undefined && json.errors !== undefined){
                var translatedErrors = {}
                var errors = json.errors
                //we try to translate the errors returned from the API.
                for(var key in errors){
                    if (errors[key] in translations)
                        translatedErrors[key] = translations[errors[key]]
                    else
                        translatedErrors[key] = errors[key]
                }
                this.setState({status: 'pending', errors: translatedErrors})
            }
            else 
                this.setState({status: 'failed'})
        }.bind(this))
    }

    onSubmit(e) {
        var state = this.state
        e.preventDefault()
        var errors = this.validate(state.data)
        if (Object.keys(errors).length > 0){
            this.setState({errors : errors})
            return
        }
        this.setState({status : 'sending', errors: {}})
        this.submitData(state.data)
    }

    validate(data){
        var errors = {}
        var emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/i;
        if (!data.email){
            errors.email = 'Bitte geben Sie eine E-Mail Adresse an.'
        }
        if (!emailRegex.test(data.email)){
            errors.email = 'Bitte geben Sie eine gültige E-Mail Adresse an.'
        }
        if (data.name){
            var nameRegex = /^.{3,50}$/i;
            if (!nameRegex.test(data.name)){
                errors.name = 'Bitte geben Sie einen gültigen Namen an (mindestens drei Zeichen, maximal 50).'
            }
        }
        return errors
    }

    setValue(name, e){
        var data = this.state.data
        data[name] = e.target.value
        this.setState({data : data})
    }

    renderSuccess(){
        return (
            <div>
                <h2>Vielen Dank!</h2>
                <p class="alert alert-success">
                    Ihre Angaben wurden erfolgreich gespeichert.
                </p>
            </div>
        )
    }

    render(){
        if (this.state.status == 'success')
            return this.renderSuccess()
        else
            return this.renderForm()
    }

    renderForm() {
        var state = this.state
        var data = state.data
        var errors = state.errors

        function errorFor(field){
            if (!errors[field])
                return null
            return <p class="alert alert-warning">
                    {errors[field]}
                </p>
        }

        var status = this.state.status

        var failureNotice
        if (status == 'failed'){
            failureNotice = <p class="alert alert-warning">
                Beim Versenden Ihrer Daten ist leider etwas schiefgegangen. Sie können uns alternativ
                auch eine E-Mail an <a href="mailto:newsletter@kiprotect.com">newsletter@kiprotect.com</a> schicken.
                Wir bitten die Unannehmlichkeiten zu entschuldigen.
            </p>
        }

        return (
            <form ref={ c => this.form = c } id="signup" onSubmit={this.onSubmit.bind(this)}> 
                {failureNotice}                
                <fieldset disabled={!!(status === 'sending')}>
                    <div class="form-group row">
                        <label for="email" class="col-md-4 col-lg-3 col-form-label">Email</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('email')}
                            <input 
                                type="email"
                                class="form-control"
                                id="email"
                                placeholder="david.duesentrieb@muster-ag.de"
                                onChange={this.setValue.bind(this, 'email')}
                                value={data.email || ''}
                                />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="name" class="col-md-4 col-lg-3 col-form-label">Name (optional)</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('name')}
                            <input type="text"
                                   class="form-control"
                                   id="name"
                                   placeholder="David Düsentrieb"
                                   onChange={this.setValue.bind(this, 'name')}
                                   value={data.name || ''}
                            />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label class="d-xs-none col-md-4 col-lg-3 col-form-label"></label>
                        <div class="col-md-8 col-lg-9">
                            <button type="submit"
                                    class="btn btn-green btn-intro btn-lg">
                                {status == 'sending' ? 'Bitte warten...' : 'Anmelden'}
                            </button>
                        </div>
                    </div>
                </fieldset>
            </form>
        );
    }
}
$(document).ready(function(){
    var element = document.getElementById('signup-wrapper');
    element.innerHTML = '';
    render(h(App), element);
})