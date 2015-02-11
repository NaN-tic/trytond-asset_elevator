#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Building', 'ElevatorType', 'Finish', 'ManeveurType',
    'HoseType', 'Situation', 'Suspension', 'DoorType', 'Guide', 'Asset']

__metaclass__ = PoolMeta


class Building(ModelSQL, ModelView):
    'Building'
    __name__ = 'asset.building'
    name = fields.Char('Name', required=True, translate=True)

    @classmethod
    def check_xml_record(cls, records, values):
        return True


class ElevatorType(ModelSQL, ModelView):
    'Elevator Type'
    __name__ = 'asset.elevator.type'
    code = fields.Char('Code')
    name = fields.Char('Name', required=True, translate=True)

    @classmethod
    def check_xml_record(cls, records, values):
        return True

    def get_rec_name(self, name):
        if self.code:
            return '[' + self.code + '] ' + self.name
        else:
            return self.name

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('template.name',) + tuple(clause[1:]),
            ]


class Finish(ModelSQL, ModelView):
    'Finish'
    __name__ = 'asset.finish'
    name = fields.Char('Name', required=True, translate=True)


class ManeveurType(ModelSQL, ModelView):
    'Maneveur Type'
    __name__ = 'asset.maneveur.type'
    name = fields.Char('Name', required=True, translate=True)

    @classmethod
    def check_xml_record(cls, records, values):
        return True


class HoseType(ModelSQL, ModelView):
    'Hose Type'
    __name__ = 'asset.hose.type'
    name = fields.Char('Name', required=True, translate=True)


class Situation(ModelSQL, ModelView):
    'Situation'
    __name__ = 'asset.situation'
    name = fields.Char('Name', required=True, translate=True)

    @classmethod
    def check_xml_record(cls, records, values):
        return True


class Suspension(ModelSQL, ModelView):
    'Suspension Type'
    __name__ = 'asset.suspension.type'
    name = fields.Char('Name', required=True, translate=True)

    @classmethod
    def check_xml_record(cls, records, values):
        return True


class DoorType(ModelSQL, ModelView):
    'Door Type'
    __name__ = 'asset.door.type'
    name = fields.Char('Name', required=True, translate=True)


class Guide(ModelSQL, ModelView):
    'Guide'
    __name__ = 'asset.guide'
    name = fields.Char('Name', required=True, translate=True)
    type = fields.Selection([
            ('cabin', 'Cabin'),
            ('counterweight', 'Counterweight'),
            ], 'Type', required=True)

    @staticmethod
    def default_type():
        return 'cabin'

_STATES = {
    'invisible': Eval('type') != 'elevator',
    }
_DEPENDS = ['type']


class Asset:
    __name__ = 'asset'
    registry_number = fields.Char('R.A.E.', help='Elevator machine number',
        states=_STATES, depends=_DEPENDS)
    material_brand = fields.Many2One('product.brand', 'Material brand',
        states=_STATES, depends=_DEPENDS)
    provenance = fields.Selection([
            ('', ''),
            ('new_work', 'New Work'),
            ('old_work', 'Old Work'),
            ('another_conservative', 'Another conservative')], 'Proveanence',
        states=_STATES, depends=_DEPENDS)
    elevator_type = fields.Many2One('asset.elevator.type', 'Type',
        states=_STATES, depends=_DEPENDS)
    building = fields.Many2One('asset.building', 'Building', states=_STATES,
        depends=_DEPENDS)
    stops = fields.Integer('Stops', states=_STATES, depends=_DEPENDS)
    payload = fields.Integer('Payload', states=_STATES, depends=_DEPENDS)
    persons = fields.Integer('Persons', states=_STATES, depends=_DEPENDS)
    velocity = fields.Float('Velocity', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    landing_door_type = fields.Many2One('asset.door.type', 'Landing door type',
        states=_STATES, depends=_DEPENDS)
    hand = fields.Selection([
            ('', ''),
            ('left', 'Left'),
            ('right', 'Right'),
            ], 'Hand', states=_STATES, depends=_DEPENDS)
    light_height = fields.Float('Height', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    light_width = fields.Float('Width', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    doors_number = fields.Integer('Doors Number', states=_STATES,
        depends=_DEPENDS)
    doors_brand = fields.Many2One('product.brand', 'Doors brand',
        states=_STATES, depends=_DEPENDS)
    doors_product = fields.Many2One('product.product', 'Doors Product',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    locks_brand = fields.Many2One('product.brand', 'Locks brand',
        states=_STATES, depends=_DEPENDS)
    cabin_depth = fields.Float('Depth', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    cabin_width = fields.Float('Width', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    cabin_accesses = fields.Integer('Cabin Accesses', states=_STATES,
        depends=_DEPENDS)
    cabin_doors = fields.Integer('Cabin Doors', states=_STATES,
        depends=_DEPENDS)
    cabin_doors_module = fields.Char('Cabin Doors Module', states=_STATES,
        depends=_DEPENDS)
    lateral_finish = fields.Many2One('asset.finish', 'Lateral Finish',
        states=_STATES, depends=_DEPENDS)
    ground_finish = fields.Many2One('asset.finish', 'Ground Finish',
        states=_STATES, depends=_DEPENDS)
    roof_finish = fields.Many2One('asset.finish', 'Roof Finish',
        states=_STATES, depends=_DEPENDS)
    phone = fields.Char('Phone', states=_STATES, depends=_DEPENDS)
    door_motor_brand = fields.Many2One('product.brand', 'Door Motor Brand',
        states=_STATES, depends=_DEPENDS)
    door_motor_product = fields.Many2One('product.product',
        'Door Motor Product', states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    maneveur_type = fields.Many2One('asset.maneveur.type', 'Maneveur Type',
        states=_STATES, depends=_DEPENDS)
    manevuer_manufacturer = fields.Many2One('party.party',
        'Manevuer Manufacturer', states=_STATES, depends=_DEPENDS)
    input_voltage = fields.Integer('Input Voltage', states=_STATES,
        depends=_DEPENDS, help='Voltage at the entrance of the property (in '
        'volts')
    lleva_voltage = fields.Integer('Lleva Voltage', states=_STATES,
        depends=_DEPENDS, help='Lleva voltage (in volts)')
    brake_voltage = fields.Integer('Brake Voltage', states=_STATES,
        depends=_DEPENDS, help='Brake voltage (in volts)')
    contactor_types = fields.Many2One('product.product', 'Contactor Types',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    contactor_voltage = fields.Integer('Contactor Voltage', states=_STATES,
        depends=_DEPENDS, help='Contactor voltage (in volts)')
    hose_type = fields.Many2One('asset.hose.type', 'Hose Type',
        states=_STATES, depends=_DEPENDS)
    number_of_conductors = fields.Integer('Number of conductors',
        states=_STATES, depends=_DEPENDS)
    conductors_length = fields.Integer('Conductors Length', states=_STATES,
        depends=_DEPENDS)
    conductors_connection = fields.Selection([
            ('', ''),
            ('CM', 'CM'),
            ('MC', 'MC'),
            ], 'Conductors Connection', states=_STATES, depends=_DEPENDS)
    situation = fields.Many2One('asset.situation', 'Situation', states=_STATES,
        depends=_DEPENDS)
    buttons_brand = fields.Many2One('product.brand', 'Buttons brand',
        states=_STATES, depends=_DEPENDS)
    buttons_product = fields.Many2One('product.product', 'Buttons product',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    cabin_buttons = fields.Char('Cabin Buttons', states=_STATES,
        depends=_DEPENDS)
    main_buttons = fields.Char('Main Floor Buttons', states=_STATES,
        depends=_DEPENDS)
    other_buttons = fields.Char('Other floors Buttons', states=_STATES,
        depends=_DEPENDS)
    ligths_voltage = fields.Integer('Ligths Voltage', states=_STATES,
        depends=_DEPENDS, help='Ligths voltage (in volts)')
    displays_brand = fields.Many2One('product.brand', 'Displays brand',
        states=_STATES, depends=_DEPENDS)
    displays_product = fields.Many2One('product.product', 'Displays product',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    bidirectional_brand = fields.Many2One('product.brand',
        'Bidirectional brand', states=_STATES, depends=_DEPENDS)
    bidirectional_product = fields.Many2One('product.product',
        'Bidirectional product', states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    gsm = fields.Boolean('GSM', states=_STATES, depends=_DEPENDS)
    machine_brand = fields.Many2One('product.brand', 'Machine brand',
        states=_STATES, depends=_DEPENDS)
    machine_product = fields.Many2One('product.product', 'Machine product',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    pulley = fields.Integer('Pulley', states=_STATES, depends=_DEPENDS,
        help='Milimeters of the pulley diamenter')
    power = fields.Float('Power', digits=(16, 2), states=_STATES,
        depends=_DEPENDS, help='Power (in kw)')
    rpm_motor = fields.Integer('RPM Motor', states=_STATES, depends=_DEPENDS)
    wire_number = fields.Integer('Wire number', states=_STATES,
        depends=_DEPENDS)
    wire_diameter = fields.Integer('Wire diameter', states=_STATES,
        depends=_DEPENDS)
    wire_lenght = fields.Integer('Wire lenght', states=_STATES,
        depends=_DEPENDS)
    deflection_pulley = fields.Boolean('Deflection pulley', states=_STATES,
        depends=_DEPENDS)
    brake_brand = fields.Many2One('product.brand', 'Brake Brand',
        states=_STATES, depends=_DEPENDS)
    cilinder_brand = fields.Many2One('product.brand', 'Cilinder Brand',
        states=_STATES, depends=_DEPENDS)
    path_length = fields.Float('Path Length', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    door_width = fields.Float('Door Width', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    door_height = fields.Float('Door Height', digits=(16, 2), states=_STATES,
        depends=_DEPENDS)
    suspension_type = fields.Many2One('asset.suspension.type',
        'Suspension Type', states=_STATES, depends=_DEPENDS)
    hose_diameter = fields.Integer('Hose diameter', states=_STATES,
        depends=_DEPENDS)
    hose_lenght = fields.Integer('Hose lenght', states=_STATES,
        depends=_DEPENDS)
    cabin_guides = fields.Many2One('asset.guide', 'Cabin Guides',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '=', 'cabin'),
            ])
    counterweight_product = fields.Many2One('product.product',
        'Counterweight Product', states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    counterweight_guides = fields.Many2One('asset.guide',
        'Counterweight Guides', states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '=', 'counterweight'),
            ])
    limiter_brand = fields.Many2One('product.brand', 'Limiter Brand',
        states=_STATES, depends=_DEPENDS)
    limiter_diameter = fields.Integer('Limiter Diamater', states=_STATES,
        depends=_DEPENDS)
    limiter_wire_diameter = fields.Integer('Limiter Wire Diamater',
        states=_STATES, depends=_DEPENDS)
    limiter_wire_lenght = fields.Integer('Limiter Wire Length', states=_STATES,
        depends=_DEPENDS)
    cabin_chassis_brand = fields.Many2One('product.brand',
        'Cabin chasis brand', states=_STATES, depends=_DEPENDS)
    cabin_chassis_product = fields.Many2One('product.product',
        'Cabin chasis product',
        states=_STATES, depends=_DEPENDS,
        domain=[
            ('type', '!=', 'service'),
            ])
    parachute_brand = fields.Many2One('product.brand', 'Parachute brand',
        states=_STATES, depends=_DEPENDS)
    parachute_counterweight = fields.Boolean('Parachute counterweight',
        states=_STATES, depends=_DEPENDS)
    notes = fields.Text('Notes', states=_STATES, depends=_DEPENDS)
    manufacturer = fields.Many2One('party.party', 'Manufacturer',
        states=_STATES, depends=_DEPENDS)
    conservative = fields.Many2One('party.party', 'Conservative',
        states=_STATES, depends=_DEPENDS)
    general_state = fields.Char('General State', states=_STATES,
        depends=_DEPENDS)
    reformed = fields.Boolean('Reformed', states=_STATES, depends=_DEPENDS)
    in_normative = fields.Boolean('In Normative', states=_STATES,
        depends=_DEPENDS)
    piston_diameter = fields.Integer('Piston diameter', states=_STATES,
        depends=_DEPENDS)

    @classmethod
    def __setup__(cls):
        super(Asset, cls).__setup__()
        elevator = ('elevator', 'Elevator')
        if not elevator in cls.type.selection:
            cls.type.selection.append(elevator)

    @staticmethod
    def default_provenance():
        return ''

    @staticmethod
    def default_hand():
        return ''

    @staticmethod
    def default_conductors_connection():
        return ''
