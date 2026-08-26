from odoo import models, fields

class PinjamBuku(models.Model):
    _name = 'pinjam.buku'
    _description = 'Transaksi Peminjaman Buku'

    nomor_pinjam = fields.Char(string='Nomor Pinjam', required=True)
    

    member_id = fields.Many2one('perpustakaan.member', string='Siswa / Member', required=True)
    
    buku_id = fields.Many2one('data.buku', string='Buku', required=True)
    tanggal_pinjam = fields.Date(string='Tanggal Pinjam', default=fields.Date.today)
    tanggal_pengembalian = fields.Date(string='Tanggal Pengembalian')