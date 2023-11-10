from flask import render_template, url_for, redirect, request, flash, session
from application.forms import EmployeeForm, SearchForm, EmailForm
from application.models import employee
from application import app, db
from flask_mail import Message, Mail
from sqlalchemy import or_, func


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'szymon.turek6969@gmail.com' 
app.config['MAIL_PASSWORD'] = 'agata102' 
mail = Mail(app)

@app.route('/tool', methods=['GET', 'POST'])
def tool():

    form = EmployeeForm()
    search_form = SearchForm(request.form) 
    employees = employee.query.all()


    if request.method == 'POST':
        if search_form.validate_on_submit():
            search_term = search_form.search.data
           
            employees = employee.query.filter(or_(
                employee.first_name.ilike(f"%{search_term}%"),
                employee.last_name.ilike(f"%{search_term}%")
            )).all()


    if form.first_name.data:

        employee_data = employee(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    birth_day=form.birth_day.data,
                    adres=form.adres.data,
                    phone_number=form.phone_number.data,
                    salary=form.salary.data,
                    position=form.position.data,
                    email=form.first_name.data + '.' + form.last_name.data + '@company.com'
                    )

        db.session.add(employee_data)
        db.session.commit()
        flash('Employee successfully added!')
        return redirect(url_for('tool'))
    
    position_counts = db.session.query(employee.position, func.count(employee.id)).group_by(employee.position).all()

    return render_template('tool.html', employees=employees, form=form, search_form=search_form, position_counts=position_counts)

@app.route('/tool-delete/<int:employee_id>', methods=['GET', 'POST'])
def delete_employee(employee_id):
    employee_to_delete = employee.query.get(employee_id)
    if employee_to_delete:
        db.session.delete(employee_to_delete)
        db.session.commit()
        flash
    return redirect(url_for('tool'))


@app.route('/mail', methods=['GET', 'POST'])
def mail():
    form = EmployeeForm()
    search_form = SearchForm(request.form)
    email_form = EmailForm()
    employees = employee.query.all()
    recipients = []

    if request.method == 'POST':
        if search_form.validate_on_submit():
            search_term = search_form.search.data
            employees = employee.query.filter(or_(
                employee.first_name.ilike(f"%{search_term}%"),
                employee.last_name.ilike(f"%{search_term}%")
            )).all()
    elif email_form.validate_on_submit():
           
            recipients = request.form.getlist('selected_employees')
            subject = email_form.subject.data
            message = email_form.message.data

            msg = Message(subject, sender='szymon.turek6969@gmail.com', recipients=recipients)
            msg.body = message
            mail.send(msg)
            flash('Email has been sent!')
            return redirect(url_for('mail'))

    return render_template('mail.html', employees=employees, form=form, search_form=search_form, email_form=email_form, recipients=recipients)



    






