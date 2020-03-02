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

String.prototype.format = function () {
    "use strict";
    var str = this.toString();

    var t = typeof arguments[0];
    var args
    if (arguments.length == 0)
        args = {}
    else
        args = ("string" === t || "number" === t) ?
                Array.prototype.slice.call(arguments)
                : arguments[0];

    var splits = []

    var s = str
    while(s.length > 0){    
        var m = s.match(/\{(?!\{)([\w\d]+)\}(?!\})/)
        if (m !== null){
            var left = s.substr(0, m.index)
            var sep = s.substr(m.index, m[0].length)
            s = s.substr(m.index+m[0].length)
            var n = parseInt(m[1])
            splits.push(left)
            if (n != n){ // not a number
                splits.push(args[m[1]])
            } else { // a numbered argument
                splits.push(args[n])
           }
        } else {
            splits.push(s)
            s = ""
        }    
    }
    return splits
};

function t(key){
    var str = translations[window.language][key]
    if (str === undefined)
        return "[no translation available for key "+key+"]"
    var formattedStr = str.format(...Array.prototype.slice.call(arguments, 1))
    return formattedStr
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
            url: "https://auth.kiprotect.com/api/newsletter/v1/subscribe/beta",
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
            errors.email = t('email-missing')
        }
        if (!emailRegex.test(data.email)){
            errors.email = t('email-invalid')
        }
        var companyRegex = /^.{3,50}$/i;
        if (!data.company){
            errors.company = t('company-name-missing')
        }
        if (!companyRegex.test(data.company)){
            errors.company = t('company-name-invalid')
        }
        var nameRegex = /^.{3,50}$/i;
        if (!data.name){
            errors.name = t('contact-name-invalid')
        }
        if (!nameRegex.test(data.name)){
            errors.name = t('contact-name-invalid')
        }
        var phoneRegex = /^[0-9\-\/\+]{3,50}$/i;
        if (data.phone){
            //validate the phone number
            if (!phoneRegex.test(data.phone)){
                errors.phone = t('phone-number-invalid')
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
                <h2>{t('thanks')}</h2>
                <p class="alert alert-success">
                    {t('data-has-been-saved')}
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
                {t('something-went-wrong', {email : <a href={'mailto:'+t('signup-email')}>{t('signup-email')}</a>})}
            </p>
        }

        return (
            <form ref={ c => this.form = c } id="signup" onSubmit={this.onSubmit.bind(this)}> 
                {failureNotice}                
                <fieldset disabled={!!(status === 'sending')}>
                    <div class="form-group row">
                        <label for="email" class="col-md-4 col-lg-3 col-form-label">{t('email')}</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('email')}
                            <input 
                                type="email"
                                class="form-control"
                                id="email"
                                placeholder={t('email-placeholder')}
                                onChange={this.setValue.bind(this, 'email')}
                                value={data.email || ''}
                                />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="company" class="col-md-4 col-lg-3 col-form-label">{t('company-name')}</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('company')}
                            <input type="text"
                                   class="form-control"
                                   id="company"
                                   placeholder={t('company-placeholder')}
                                   onChange={this.setValue.bind(this, 'company')}
                                   value={data.company || ''}
                            />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="name" class="col-md-4 col-lg-3 col-form-label">{t('contact-name')}</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('name')}
                            <input type="text"
                                   class="form-control"
                                   id="name"
                                   placeholder={t('name-placeholder')}
                                   onChange={this.setValue.bind(this, 'name')}
                                   value={data.name || ''}
                            />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="phone" class="col-md-4 col-lg-3 col-form-label">{t('phone')}</label>
                        <div class="col-md-8 col-lg-9">
                            {errorFor('phone')}
                            <input type="phone"
                                   class="form-control"
                                   id="phone"
                                   placeholder={t('phone-placeholder')}
                                   onChange={this.setValue.bind(this, 'phone')}
                                   value={data.phone || ''}
                            />
                        </div>
                    </div>

                    <div class="form-group row">
                        <label class="d-xs-none col-md-4 col-lg-3 col-form-label"></label>
                        <div class="col-md-8 col-lg-9">
                            <button type="submit"
                                    class="btn btn-green btn-intro btn-md">
                                {status == 'sending' ? t('please-wait') : t('submit')}
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
