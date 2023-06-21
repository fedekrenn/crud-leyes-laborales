from mysql.connector import Error
import utils.format_data as format_data

class Database():

    def __init__(self, db):
        self.db = db
        self.mycursor = db.cursor()

    def get_all_laws(self):
        try:
            self.mycursor.execute("SELECT leyes.nro_registro, leyes.nro_normativa, leyes.fecha, leyes.palabras_clave, leyes.descripcion, tipos_normativa.tipo_normativa, categorias.categoria, jurisdicciones.jurisdiccion, organos_legislativos.organo_legislativo FROM leyes JOIN tipos_normativa ON leyes.tipos_normativa_id_tipo_normativa = tipos_normativa.id_tipo_normativa JOIN categorias ON leyes.categorias_id_categoria = categorias.id_categoria JOIN jurisdicciones ON leyes.jurisdicciones_id_jurisdiccion = jurisdicciones.id_jurisdiccion JOIN organos_legislativos ON leyes.organos_legislativos_id_organo_legislativo = organos_legislativos.id_organo_legislativo")
            result = self.mycursor.fetchall()
            if len(result) > 0:
                return format_data.format_data(result)
            else:
                print("No hay leyes")
        except Error:
            print(f"Hubo un error, {Error}")