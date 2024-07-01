from django.db.models import TextChoices


class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULAS_MOTOR = "TVM", "Trocar valvulas do motor"
    TROCA_OLEO = "TO", "Troca de oleo"
    BALANCEAMENTO = "B", "Balanceamento"

