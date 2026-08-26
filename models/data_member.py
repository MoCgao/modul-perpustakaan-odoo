from odoo import models, fields

class DataMember(models.Model):
    _name = 'data.member'
    _description = 'Data Member'

    name = fields.Char(string='Nama Member', required=True)

    member_id = fields.Char(string='Member ID', required=True)
    siswa_id = fields.Many2one('data.siswa', string='Nama Siswa', required=True)
    tanggal_daftar = fields.Date(string='Tanggal Daftar', default=fields.Date.today)
    
    # Pastikan penulisan Selection seperti ini (tanpa ada variabel bernama Selection di atasnya)
    status = fields.Selection([
        ('aktif', 'Aktif'),
        ('non_aktif', 'Non Aktif')
    ], string='Status', default='aktif', required=True)
    
    batas_pinjam = fields.Integer(string='Batas Pinjam', default=3)