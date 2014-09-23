#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Building', 'ElevatorType', 'Finish', 'ManeveurType', 'HoseType',
    'Situation', 'Suspension', 'DoorType', 'Guide', 'Elevator']


class Building(ModelSQL, ModelView):
    'Building'
    __name__ = 'asset.building'
    name = fields.Char('Name', required=True, translate=True)


class ElevatorType(ModelSQL, ModelView):
    'Elevator Type'
    __name__ = 'asset.elevator.type'
    code = fields.Char('Code')
    name = fields.Char('Name', required=True)

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


class HoseType(ModelSQL, ModelView):
    'Hose Type'
    __name__ = 'asset.hose.type'
    name = fields.Char('Name', required=True, translate=True)


class Situation(ModelSQL, ModelView):
    'Situation'
    __name__ = 'asset.situation'
    name = fields.Char('Name', required=True, translate=True)


class Suspension(ModelSQL, ModelView):
    'Suspension Type'
    __name__ = 'asset.suspension.type'
    name = fields.Char('Name', required=True, translate=True)


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


class Elevator(ModelSQL, ModelView):
    'Elevator'
    __name__ = 'asset.elevator'
    asset = fields.Many2One('asset', 'Asset', required=True,
        ondelete='CASCADE')
    active = fields.Function(fields.Boolean('Active'),
        'get_active', searcher='search_active')
    administrator = fields.Many2One('party.party', 'Administrator')
    code = fields.Char('Code')
    registry_number = fields.Char('R.A.E.', help='Elevator machine number')
    material_brand = fields.Many2One('product.brand', 'Material brand')
    provenance = fields.Selection([
            ('', ''),
            ('new_work', 'New Work'),
            ('old_work', 'Old Work'),
            ('another_conservative', 'Another conservative')], 'Proveanence')
    type = fields.Many2One('asset.elevator.type', 'Type')
    building = fields.Many2One('asset.building', 'Building')
    stops = fields.Integer('Stops')
    payload = fields.Integer('Payload')
    persons = fields.Integer('Persons')
    velocity = fields.Float('Velocity', digits=(16, 2))
    landing_door_type = fields.Many2One('asset.door.type', 'Landing door type')
    hand = fields.Selection([
            ('', ''),
            ('left', 'Left'),
            ('right', 'Right'),
            ], 'Hand')
    light_height = fields.Float('Height', digits=(16, 2))
    light_width = fields.Float('Width', digits=(16, 2))
    doors_brand = fields.Many2One('product.brand', 'Doors brand')
    doors_product = fields.Many2One('product.product', 'Doors Product',
        domain=[
            ('type', '!=', 'service'),
            ])
    locks_brand = fields.Many2One('product.brand', 'Locks brand')
    cabin_height = fields.Float('Height', digits=(16, 2))
    cabin_width = fields.Float('Width', digits=(16, 2))
    lateral_finish = fields.Many2One('asset.finish', 'Lateral Finish')
    ground_finish = fields.Many2One('asset.finish', 'Ground Finish')
    roof_finish = fields.Many2One('asset.finish', 'Roof Finish')
    phone = fields.Char('Phone')
    door_motor_brand = fields.Many2One('product.brand', 'Door Motor Brand')
    door_motor_product = fields.Many2One('product.product',
        'Door Motor Product',
        domain=[
            ('type', '!=', 'service'),
            ])
    maneveur_type = fields.Many2One('asset.maneveur.type', 'Maneveur Type')
    manevuer_manufacturer = fields.Many2One('party.party',
        'Manevuer Manufacturer')
    input_voltage = fields.Integer('Input Voltage', help='Voltage at the '
        'entrance of the property (in volts')
    lleva_voltage = fields.Integer('Lleva Voltage', help='Lleva voltage '
        '(in volts)')
    brake_voltage = fields.Integer('Brake Voltage', help='Brake voltage '
        '(in volts)')
    contactor_types = fields.Many2One('product.product', 'Contactor Types',
        domain=[
            ('type', '!=', 'service'),
            ])
    contactor_voltage = fields.Integer('Contactor Voltage', help='Contactor '
        'voltage (in volts)')
    hose_type = fields.Many2One('asset.hose.type', 'Hose Type')
    number_of_conductors = fields.Integer('Number of conductors')
    conductors_length = fields.Integer('Conductors Length')
    situation = fields.Many2One('asset.situation', 'Situation')
    buttons_brand = fields.Many2One('product.brand', 'Buttons brand')
    buttons_product = fields.Many2One('product.product', 'Buttons product',
        domain=[
            ('type', '!=', 'service'),
            ])
    ligths_voltage = fields.Integer('Ligths Voltage', help='Ligths voltage '
        '(in volts)')
    displays_brand = fields.Many2One('product.brand', 'Displays brand')
    displays_product = fields.Many2One('product.product', 'Displays product',
        domain=[
            ('type', '!=', 'service'),
            ])
    bidirectional_brand = fields.Many2One('product.brand',
        'Bidirectional brand')
    bidirectional_product = fields.Many2One('product.product',
        'Bidirectional product',
        domain=[
            ('type', '!=', 'service'),
            ])
    gsm = fields.Boolean('GSM')
    machine_brand = fields.Many2One('product.brand', 'Machine brand')
    machine_product = fields.Many2One('product.product', 'Machine product',
        domain=[
            ('type', '!=', 'service'),
            ])
    pulley = fields.Integer('Pulley', help='Milimeters of the pulley '
        'diamenter')
    power = fields.Integer('Power', help='Power (in kw)')
    rpm_motor = fields.Integer('RPM Motor')
    wire_number = fields.Integer('Wire number')
    wire_diameter = fields.Integer('Wire diameter')
    wire_lenght = fields.Integer('Wire lenght')
    deflection_pulley = fields.Boolean('Deflection pulley')
    brake_brand = fields.Many2One('product.brand', 'Brake Brand')
    cilinder_brand = fields.Many2One('product.brand', 'Cilinder Brand')
    suspension_type = fields.Many2One('asset.suspension.type',
        'Suspension Type')
    hose_diameter = fields.Integer('Hose diameter')
    hose_lenght = fields.Integer('Hose lenght')
    cabin_guides = fields.Many2One('asset.guide', 'Cabin Guides',
        domain=[
            ('type', '=', 'cabin'),
            ])
    counterweight_guides = fields.Many2One('asset.guide',
        'Counterweight Guides',
        domain=[
            ('type', '=', 'counterweight'),
            ])
    limiter_brand = fields.Many2One('product.brand', 'Limiter Brand')
    limiter_lenght = fields.Integer('Limiter Length')
    limiter_diameter = fields.Integer('Limiter Diamater')
    cabin_chassis_brand = fields.Many2One('product.brand',
        'Cabin chasis brand')
    cabin_chassis_product = fields.Many2One('product.product',
        'Cabin chasis product',
        domain=[
            ('type', '!=', 'service'),
            ])

    parachute_brand = fields.Many2One('product.brand', 'Parachute brand')
    parachute_counterweight = fields.Boolean('Parachute counterweight')
    notes = fields.Text('Notes')

    @staticmethod
    def default_provenance():
        return ''

    @staticmethod
    def default_hand():
        return ''

    def get_rec_name(self, name):
        return self.asset.name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('asset.name',) + tuple(clause[1:])]

    def get_active(self, name):
        return self.asset.active

    @classmethod
    def search_active(cls, name, clause):
        return [('asset.active',) + tuple(clause[1:])]
