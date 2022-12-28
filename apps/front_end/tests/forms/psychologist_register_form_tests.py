from django.test import TestCase
from apps.front_end.forms import PsychologistRegisterForm
from parameterized import parameterized


class PsychologistRegisterFormTest(TestCase):
    @parameterized.expand(
        [
            ("crp_register", "Registro profissional:"),
            ("short_description", "Descrição curta/titulação:"),
            ("professional_address", "Endereço profissional:"),
            ("city", "Cidade de atendimento:"),
            ("secondary_address", "Endereço secundário:"),
            ("phone_number", "Telefone profissional:"),
            ("cpf", "CPF/CNPJ:"),
            ("instagram_link", "Link perfil Instagram:"),
            ("twitter_link", "Link perfil Twitter:"),
            ("linkedin_link", "Link perfil LinkedIn:"),
            ("whatsapp_number", "WhatsApp:"),
            ("bio", "Biografia/Descrição longa:"),
            ("schedule_description", "Agenda/horários de atendimento:"),
            ("photo", "Foto de perfil:"),
        ]
    )
    def test_fields_labels_is_correct(self, field_name, expected_label):
        form = PsychologistRegisterForm()
        current_label = form[field_name].field.label
        self.assertEqual(current_label, expected_label)
