def test_medicament():
    medicament = Medicament("1", "nume", "prod", 43, "necesita reteta")
    assert medicament.id_entity == "1"
    assert medicament.nume_medicament == "nume"
    assert medicament.pret_medicament == "prod"
    assert medicament.pret_medicament == 43
    assert medicament.reteta_medicament == "necesita reteta"


def test_card_client():
    card_client = Card_client("1", "nume", "pren", 2345,
                              "2021-2-2", "2021-2-3")
    assert card_client.id_entity == "1"
    assert card_client.nume_card_client == "nume"
    assert card_client.prenume_card_client == "pren"
    assert card_client.CNP_card_client == "2345"
    assert card_client.data_nasterii_card_client == "2021-2-2"
    assert card_client.data_inregistrarii_card_client == "2021-2-3"


def test_tranzactie():
    tranzactie = Tranzactie("1", "1", "1", 56, "2021-8-9", "21:23")
    assert tranzactie.id_entity == "1"
    assert tranzactie.id_medicament == "1"
    assert tranzactie.id_card_client == "1"
    assert tranzactie.nr_bucati == 56
    assert tranzactie.data == "21:23"
    assert tranzactie.ora == "21:23"