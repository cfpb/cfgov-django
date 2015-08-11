import os

from django.views.generic import View
from django.http import HttpResponse
from core.lib.PDFreactor import *


class PDFGeneratorView(View):
    render_url = None
    stylesheet_url = None
    filename = None
    license = os.environ.get('PDFREACTOR_LICENSE')

    def get_render_url(self):
        if self.render_url is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'render_url' or an implementation of 'get_render_url()'")
        return self.render_url

    def get_stylesheet_url(self):
        if self.stylesheet_url is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'stylesheet_url' or an implementation of 'get_stylesheet_url()'")
        return self.stylesheet_url

    def get_filename(self):
        if self.filename is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'filename' or an implementation of 'get_filename()'")
        return self.filename

    def generate_pdf(self):
        if self.license is None:
            raise Exception("PDFGeneratorView requires a license")
        pdf_reactor = PDFreactor()
        pdf_reactor.setLogLevel(PDFreactor.LOG_LEVEL_WARN)
        pdf_reactor.setLicenseKey(self.license)
        pdf_reactor.setAuthor('CFPB')
        pdf_reactor.setAddTags(True)
        pdf_reactor.setAddBookmarks(True)
        pdf_reactor.addUserStyleSheet('', '', '', self.get_stylesheet_url())
        query_string = self.request.GET.urlencode()
        result = \
            pdf_reactor.renderDocumentFromURL('{0}?{1}'.format(
                self.get_render_url(),
                query_string))
        # Check if successful
        if result is None:
            # Not successful, return 500
            raise Exception('Error while rendering PDF: {}'.format(
                pdf_reactor.getError()))
        else:
            # Set the correct header for PDF output
            response = HttpResponse(result, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(
                self.get_filename())
            return response

    def get(self, *args, **kwargs):
        return self.generate_pdf()
