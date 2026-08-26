from odoo import models, fields

class DataBuku(models.Model):
    _name = 'data.buku'
    _description = 'Data Buku Perpustakaan'

    judul_buku = fields.Char(string='Judul Buku', required=True)
    penulis = fields.Char(string='Penulis', required=True)
    penerbit = fields.Char(string='Penerbit')
    tahun_terbit = fields.Integer(string='Tahun Terbit')
    jumlah_halaman = fields.Integer(string='Jumlah Halaman')
    kategori = fields.Char(string='Kategori')