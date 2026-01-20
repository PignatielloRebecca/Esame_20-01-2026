from database.DB_connect import DBConnect
from model.artist import Artist
from model.generi import Generi

class DAO:



    @staticmethod
    def read_all_artists(numero):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select a.id as id, a.name as name
                    from artist a, album al 
                    where a.id=al.artist_id 
                    group by a.id, a.name 
                    having count(*)>=%s
                """
        cursor.execute(query, (numero,))
        for row in cursor:
            artist = Artist(row['id'],row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result
    @staticmethod

    def read_all_genere(numero):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """with ArtistiSelezionati as (select a.id , a.name 
            from artist a, album al 
            where a.id=al.artist_id 
            group by a.id, a.name 
            having count(*)>=%s)

            select distinct  a.id, a.name as nome, g.name as genere
            from artist a, album al, track t, genre g  
            where a.id=al.artist_id  and al.id=t.album_id and t.genre_id= g.id  and a.id in (select id from ArtistiSelezionati)"""
        cursor.execute(query, (numero,))
        for row in cursor:
            genere = Generi(row['id'],row['nome'], row['genere'])
            result.append(genere)
        cursor.close()
        conn.close()
        return result




