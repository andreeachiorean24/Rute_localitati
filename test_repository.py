from Repository.json_repository import JsonRepository
from utils import clear_file


def test_medicament_repository():
    filename = 'test_medicamente.json'
    clear_file(filename)
    medicament_repository = JsonRepository(filename)
    added = Medicament('1', 'nume1', 'prod1', 34, 'nu necesita reteta')
    medicament_repository.create(added)
    assert medicament_repository.read(added.id_entity) == added

    updated = Medicament('1', 'nume2', 'prod2', 90, 'necesita reteta')
    medicament_repository.update(updated)
    assert medicament_repository.read(updated.id_entity) == updated

    added2 = Medicament('2', 'nm', 'prod', 23, 'nu necesita reteta')
    medicament_repository.create(added2)
    assert medicament_repository.read(added2.id_entity) == added2

    id_entity = added2.id_entity
    medicament_repository.delete(id_entity)
    assert medicament_repository.read(id_entity) is None


def test_card_repository():
    filename = 'test_carduri_client.json'
    clear_file(filename)
    card_repository = JsonRepository(filename)
    added = Card_client('9', 'nume1', 'pren1',
                        '25363', 2021-2-2, 2022-2-2)
    card_repository.create(added)
    assert card_repository.read(added.id_entity) == added

    updated = Card_client('9', 'nume2', 'pren2',
                          '23', 2021-4-5, 2022-3-3)
    card_repository.update(updated)
    assert card_repository.read(updated.id_entity) == updated

    added2 = Card_client('2', 'nm', 'pr',
                         '45', 2020-3-4, 2023-3-4)
    card_repository.create(added2)
    assert card_repository.read(added2.id_entity) == added2

    id_entity = added2.id_entity
    card_repository.delete(id_entity)
    assert card_repository.read(id_entity) is None


def test_transaction_repository():
    filename = 'test_tranzactii.json'
    clear_file(filename)
    tranzactie_repository = JsonRepository(filename)
    added = Tranzactie('1', '1', '1', 23, 2021-2-2, '23:00')
    tranzactie_repository.create(added)
    assert tranzactie_repository.read(added.id_entity) == added

    updated = Tranzactie('1', '2', '1', 45, 2021-4-5, '12')
    tranzactie_repository.update(updated)
    assert tranzactie_repository.read(added.id_entity) == updated

    added2 = Tranzactie('2', '1', '1', 22, 2023-2-2, '13:12')
    tranzactie_repository.create(added2)
    assert tranzactie_repository.read(added2.id_entity) == added2
    id_entity = added2.id_entity
    tranzactie_repository.delete(id_entity)
    assert tranzactie_repository.read(id_entity) is None
