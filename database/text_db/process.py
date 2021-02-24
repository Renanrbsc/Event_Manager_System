def append_model(local_name: str, model: object):
    with open(f"database\\imports\\txt\\{local_name}.txt", "a") as txt:
        txt.write(str(model))
        print(f"Registro salvo com sucesso!")


def read_id(local_name: str, model: object) -> str or None:
    with open(f"database\\imports\\txt\\{local_name}.txt", "r") as txt:
        for row in txt:
            row_data = row.strip('\n')
            row_data = row_data.split(',')

            if model.getId() == row_data[0]:
                print(f"Registro encontrado!")
                return row
    return None


def read_all(local_name: str) -> str or None:
    all_data = list()
    with open(f"database\\imports\\txt\\{local_name}.txt", "r") as txt:
        for row in txt:
            data_row = row.strip('\n')
            all_data.append(data_row)
    return all_data
