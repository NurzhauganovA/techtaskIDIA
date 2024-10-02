from odoo import models, fields, api


class Product(models.Model):
    _name = 'product_module.product'
    _description = 'Product'

    name = fields.Char(string="Product Name", required=True)
    color = fields.Char(string="Color")
    delivery_date = fields.Date(string="Delivery Date")
    price = fields.Float(string="Price", required=True)
    quantity = fields.Integer(string="Quantity")
    height = fields.Float(string="Height")
    width = fields.Float(string="Width")
    depth = fields.Float(string="Depth")
    volume = fields.Float(string="Volume", compute="_compute_volume")

    @api.depends('height', 'width', 'depth')
    def _compute_volume(self):
        for record in self:
            record.volume = record.height * record.width * record.depth

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 0:
                raise models.ValidationError("Price cannot be negative!")

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 0:
                raise models.ValidationError("Quantity cannot be negative!")

    @api.constrains('height', 'width', 'depth')
    def _check_dimensions(self):
        for record in self:
            if record.height < 0 or record.width < 0 or record.depth < 0:
                raise models.ValidationError("Dimensions cannot be negative!")

    @api.constrains('volume')
    def _check_volume(self):
        for record in self:
            if record.volume < 0:
                raise models.ValidationError("Volume cannot be negative!")
