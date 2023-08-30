from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    options = {
        'background': True
    }
    pdf = pdfkit.from_string(html, options=options)
    return HttpResponse(pdf, content_type='application/pdf')
