from odoo import fields, models, api


class DataSiswa(models.Model):
    _name = 'data.siswa'
    _description = 'Data Siswa'
    _rec_name = 'nama_siswa '

    name = fields.Char(string='Nama Siswa', required=True)
    nis = fields.Char(string='NIS')
    kelas = fields.Char(string='Kelas')
