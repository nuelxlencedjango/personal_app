from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa



def pdfFiles(template_source,context_dict={}):
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")