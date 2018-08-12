from datetime import datetime

from app import db, EquipmentStatus


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    address = db.Column(db.String(256))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    departments = db.relationship('Department', backref='district', lazy='dynamic')
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<District %r>' % (self.name)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    fd_id = db.Column(db.String(128), index=True)
    address = db.Column(db.String(256))
    email_address = db.Column(db.String(128))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    stations = db.relationship('Station', backref='department', lazy='dynamic')
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

    def __repr__(self):
        return '<Department %r>' % (self.name)


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    abbreviation = db.Column(db.String(128))
    address = db.Column(db.String(256))
    email_address = db.Column(db.String(128))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    trucks = db.relationship('Truck', backref='station', lazy='dynamic')
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return '<Department %r>' % (self.name)


class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    radio_id = db.Column(db.String(128), index=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    compartments = db.relationship('Compartment', backref='truck', lazy='dynamic')
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))

    ### future upgrade and tracks where truck is, and when it last beamed up!
    position_address = db.Column(db.String(256))
    position_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # whe
    contact_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    ### end future feature

    def __repr__(self):
        return '<Truck %r>' % (self.name)


class Compartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    equipments = db.relationship('Equipment', backref='compartment', lazy='dynamic')
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'))

    def __repr__(self):
        return '<Compartment %r>' % (self.name)


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    serial_number = db.Column(db.String(128))
    capital_equipment = db.Column(db.String(128))
    description = db.Column(db.String(512))
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    compartment_id = db.Column(db.Integer, db.ForeignKey('compartment.id'))

    last_checked_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Equipment %r>' % (self.name)


class EquipmentCheckLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer)
    status = db.Column(db.Enum(EquipmentStatus), default=EquipmentStatus.PRESENT)
    notes = db.Column(db.String(512))
    compartment_id = db.Column(db.Integer)
    truck_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)
    district_id = db.Column(db.Integer)
    created_ts = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<EquipmentCheckLog %r>' % (self.name)

