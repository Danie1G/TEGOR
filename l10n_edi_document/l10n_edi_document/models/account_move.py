# Copyright 2020 Vauxoo
# License AGPL-3 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    l10n_edi_created_with_dms = fields.Boolean(
        "Created with DMS?", copy=False, help="Is market if the document was created with DMS."
    )

    def xml2record(self, default_account=False, analytic_account=False):
        """Called by the Documents workflow row during the creation of records by the Create EDI document button.
        Use the last attachment in the xml and fill data in records.

        :param default_account: Account that will be used in the invoice lines where the product is not fount. If it´s
        empty, is used the journal account.
        :type domain: list
        """

        return self

    def l10n_edi_document_set_partner(self, domain=None):
        """Perform a :meth:`search` followed by a :meth:`read`.

        :param domain: Search domain, Defaults to an empty domain that will match all records.
        :type domain: list

        :return: True or False
        :rtype: bool"""
        self.ensure_one()
        partner = self.env["res.partner"]

        xml_partner = partner.search(domain, limit=1)
        if not xml_partner:
            return False

        self.partner_id = xml_partner
        self._onchange_partner_id()
        return True

    def _get_edi_document_errors(self):
        # Overwrite for each country and document type
        self.ensure_one()
        return []

    def collect_taxes(self, taxes_xml):
        """Get tax data of the Impuesto node of the xml and return
        dictionary with taxes datas
        :param taxes_xml: Impuesto node of xml
        :type taxes_xml: etree
        :return: A list with the taxes data
        :rtype: list
        """
        return []


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends("product_id")
    def _compute_product_uom_id(self):
        dms = self.filtered(
            lambda l: l.move_id.l10n_edi_created_with_dms
            and l.product_id
            and l.display_type not in ("line_section", "line_note")
        )
        return super(AccountMoveLine, self - dms)._compute_product_uom_id()

    @api.depends("product_id", "product_uom_id")
    def _compute_price_unit(self):
        dms = self.filtered(
            lambda l: l.move_id.l10n_edi_created_with_dms
            and l.product_id
            and l.display_type not in ("line_section", "line_note")
        )
        return super(AccountMoveLine, self - dms)._compute_price_unit()

    @api.depends("product_id", "product_uom_id")
    def _compute_tax_ids(self):
        dms = self.filtered(
            lambda l: l.move_id.l10n_edi_created_with_dms
            and l.product_id
            and l.display_type not in ("line_section", "line_note")
        )
        return super(AccountMoveLine, self - dms)._compute_tax_ids
