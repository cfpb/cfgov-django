from core.services import PDFGeneratorView


class LeadershipCalendarPDFView(PDFGeneratorView):
    render_url = 'http://localhost/the-bureau/leadership-calendar/print/'
    stylesheet_url = 'http://localhost/static/css/pdfreactor-fonts.css'
    filename = 'cfpb_leadership-calendar.pdf'
