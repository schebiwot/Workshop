from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin
from flask_mail import Mail, Message
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# path to database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///workshop.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Top Secret'

app.config['TESTING'] = False

# email configuration

app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '67047c3e7f5964'
app.config['MAIL_PASSWORD'] = 'f651cea5353f8c'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
# IF APP IS IN TESTING MODE,IT WONT SEND EMAILS TO RECEIPIENTS
app.config['MAIL_SUPPRESS_SENDER'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/')
def index():
    return render_template('index.html', title='Fast motors')


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    technicians = db.relationship('Truck', backref='users')


class Truck(db.Model):
    __tablename__ = 'truck'
    id = db.Column(db.Integer, primary_key=True)
    driver_name = db.Column(db.String(100), nullable=False)
    driver_Phone_number = db.Column(db.Integer, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    owner_email = db.Column(db.String(100), unique=False, nullable=False)
    truck_model = db.Column(db.String(100), db.ForeignKey('truck_model.model_no'), nullable=False)
    registration = db.Column(db.String(100), unique=True, nullable=False)
    chassis = db.Column(db.String(100), unique=True, nullable=False)
    engine_number = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    technician = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    services = db.relationship('Service', backref='truck')
    truckmodel = db.relationship("TruckModel", backref="truck", lazy=True)


class TruckModel(db.Model):
    __tablename__ = 'truck_model'
    model_no = db.Column(db.String(100), unique=False, nullable=False, primary_key=True)
    parts = db.relationship("Part", backref='truck_model', lazy=True)


class Part(db.Model):
    __tablename__ = 'parts'
    id = db.Column(db.Integer, primary_key=True)
    truck_model_id = db.Column(db.String(100), nullable=False)
    part_no = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    truck_model_id = db.Column(db.String(100), db.ForeignKey('truck_model.model_no'), nullable=False)
    service_item = db.relationship("ServiceItem", uselist=False, backref="parts")


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    service_items = db.relationship('ServiceItem', backref='service')
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'))


class ServiceItem(db.Model):
    __tablename__ = 'service_items'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.String(100), nullable=False)
    part_id = db.Column(db.String(100), unique=False, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    part_id = db.Column(db.Integer, db.ForeignKey('parts.id'))


# serialize parts table
class PartSchema(ma.Schema):
    class Meta:
        fields = ('id', 'truck_model_id', 'part_no', 'description',
                  'unit_price')
        model = Part


@app.route('/newEntry', methods=['GET', 'POST'])
@login_required
def new_entry():
    if request.form:
        # grab form data
        driver_name = request.form.get('drivername')
        driver_Phone_number = request.form.get('driverphone')
        company_name = request.form.get('companyname')
        owner_name = request.form.get('ownername')
        owner_email = request.form.get('owneremail')
        truck_model = request.form.get('truckmodel')
        registration = request.form.get('registrationnumber')
        chassis = request.form.get('chassisnumber')
        engine_number = request.form.get('enginenumber')
        mileage = request.form.get('carmileage')
        technician = request.form.get('technician')

        truck = Truck(driver_name=driver_name, driver_Phone_number=driver_Phone_number,
                      company_name=company_name, owner_name=owner_name, owner_email=owner_email,
                      truck_model=truck_model,
                      registration=registration, chassis=chassis, engine_number=engine_number, mileage=mileage,
                      technician=technician)

        db.session.add(truck)
        db.session.commit()
        flash('Truck details has been successfully added!')

    models_list = TruckModel.query.all()
    users = User.query.all()

    return render_template('./newEntry.html', title='New Entry', models=models_list, users=users)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.form:
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordHash = generate_password_hash(password)
        user = User(name=name, username=username, email=email, password=passwordHash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title="SignUp")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.form:

        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Your login credentials are not correct, try again or signup')
        return redirect(url_for('login'))
    return render_template('login.html', title="Login")


@app.route('/service', methods=['GET', 'POST'])
@login_required
def service():
    if request.form:
        parts = request.form.getlist('parts[]')
        vehicle_no = request.form.get('vehicle')
        quantities = request.form.get('quantities[]')
        vehicle = Truck.query.filter_by(id=vehicle_no).first()
        v_service = Service(truck_id=vehicle.id)

        db.session.add(v_service)
        db.session.commit()
        # Save service Items
        for part, quantity in zip(parts, quantities):
            service_part = Part.query.filter_by(part_no=part, truck_model_id=vehicle.truck_model).first()
            ob_service_items = ServiceItem(part_id=service_part.id, service_id=v_service.id, quantity=int(quantity),
                                           subtotal=int(quantity) * float(service_part.unit_price) * 1.16)
            db.session.add(ob_service_items)
            db.session.commit()

        service_items = ServiceItem.query.filter_by(service_id=v_service.id).first()

        service_part = Part.query.filter_by(id=service_items.part_id).first()
        if service_items:
            send_mail(service_items, vehicle, service_part)
    vehicles = Truck.query.all()
    return render_template('./service.html', title='Service Vehicle', vehicles=vehicles)


@app.route('/lookup-parts', methods=['GET', 'POST'])
@login_required
def lookup_rooms():
    vehicle_no = request.args.get('vehicle_no')
    vehicle = Truck.query.filter_by(id=vehicle_no).first()
    parts_list = db.engine.execute(
        "select r.* from parts r where r.truck_model_id = :model_no_param;",
        {'model_no_param': vehicle.truck_model})
    part_schema = PartSchema(many=True)
    results = part_schema.dump(parts_list, many=True)
    return {"parts": results, "model_no": vehicle.truck_model}


def send_mail(service_item, vehicle, parts):
    with mail.connect() as conn:
        msg = Message("Fast Motor Workshop Service report",
                      sender="developer@mail.com",
                      recipients=['schebiwot@gmail.com'])
        msg.body = 'Hello,\n Below is a report of the vehicle: ' + vehicle.registration + ' ' \
                      ' indicating  specific parts: ' + parts.description + ' ' \
                     ' the to be serviced, quantity:  ' + str(service_item.quantity) + ' ' \
                      ' and the total cost: ' + str(service_item.subtotal) + ' ' \
                      ' of the services to be rendered'

        conn.send(msg)
        return 'message set'


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
