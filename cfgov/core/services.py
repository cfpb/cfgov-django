from django.views.generic.base import View



class PDFGeneratorView(View):
    render_url = None
    stylesheet_url=  None
    filename = None

    def get_render_url(self):
        if self.render_url is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'render_url' or an implementation of 'get_render_url()'")

    def get_stylesheer_url(self):
        if self.stylesheet_url is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'stylesheer_url' or an implementation of 'get_stylesheer_url()'")

    def get_filename(self):
        if self.filename is None:
            raise ImproperlyConfigured(
                "PDFGeneratorView requires either a definition of "
                "'filename' or an implementation of 'get_filename()'")

    def generate_pdf(self):
        pdf_reactor = PDFreactor()
        pdf_reactor.setLogLevel(PDFreactor.LOG_LEVEL_WARN)
        pdf_reactor.setLicenseKey(PDFREACTOR_LICENSE)
        pdf_reactor.setAuthor('CFPB')
        pdf_reactor.setAddTags(True)
        pdf_reactor.setAddBookmarks(True)
        pdf_reactor.addUserStyleSheet('', '', '', self.get_stylesheet_url())
        result = \
            pdf_reactor.renderDocumentFromURL('{0}?{1}'.format(self.get_render_url(),
            self.request.query_string))
        # Check if successful
        if result is None:
            # Not successful, print error and log
            print "error was ", pdf_reactor.getError(), " log was ", \
                  pdf_reactor.getLog()
            fail_with_code_and_message('Error while rendering PDF')
        else:
            # Set the correct header for PDF output and echo PDF content
            resp = make_response(result)
            resp.mimetype = 'application/pdf'
            resp.headers["Content-Disposition"] = "attachment; filename={0}".format(filename)
            return resp

