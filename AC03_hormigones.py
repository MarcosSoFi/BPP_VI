
#Clase Hormigones
class hormigon_h: 
    """
    Según el apartado 39.2 de la Instrucción EHE): T – R/C/TM/A - Precio Unitario

    >>> horm_1   = hormigon_h("HA",30,"P",20,"I", "Hormigon Armado","Central",65.22,"2020-06-22","1")
    >>> d_horm_1 = horm_1.dname_h()
    >>> print(d_horm_1)
    >>> HA - 30/P/20/I

    """
    def __init__(self,th,rh,ch,tmh,ah,dn,metodo,precio,fecha,dosificacion):
        """
        Constructor de la clase Hormigon Unitario 

        :param th:      tipo de hormigon             HM/HA/HP
        :type  th:      :class:`string`
        :param rh:      resistencia                  20-50
        :type  rh:      :class:`int`
        :param ch:      consistencia                 S/P/B/F/L
        :type  ch:      :class:`string`
        :param tmh:     tamaño del árido             
        :type  tmh:     :class:`int`
        :param ah:      clase ambiente               I/IIa/IIb/IIIa/IIIb/IIIc
        :type  ah:      :class:`string`
        :param dn:      denominacion                
        :type  dn:      :class:`string`

        :param metodo:  metodo                
        :type  metodo:  :class:`string`
        :param precio:  precio  
        :type  precio:  :class:`float`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param dosificacion:   fecha  
        :type  dosificacion:  :class:`string``

        """       
        self.th=th
        self.rh=rh
        self.ch=ch
        self.tmh=tmh
        self.ah=ah
        self.dn=dn
        self.metodo=metodo
        self.precio=precio
        self.fecha=fecha
        self.dosificacion=dosificacion

    def dname_h(self):
        """
        Metodo para crear la designacion de los hormigones - HA - 30/P/20/I
        
        """
        dname_h=f'{self.th} - {self.rh}/{self.ch}/{self.tmh}/{self.ah}'
        return dname_h

class hormigon_hd: 
    """
    Según el apartado 39.2 de la Instrucción EHE: T – R/C/TM/A - Precio Descompuesto

    >>> horm_2   = hormigon_hd("HA",30,"B",40,"IIa", "Hormigon Armado","Obra","2020-06-22",113.19,21.2,11.2,0.17,0.42,0.85)
    >>> d_horm_2 = horm_2.dname_h()
    >>> p_horm_2 = horm_2.dprecio_m()
    >>> print(d_horm_2)
    >>> HA - 30/B/40/IIa
    >>> print(p_horm_2)
    >>> 37.6663

    """
    def __init__(self,th,rh,ch,tmh,ah,dn,metodo,fecha,pcem,pare,pgrav,dcem,dare,dgrav):
        """
        Constructor de la clase Hormigon Descompuesto 

        :param th:      tipo de hormigon             HM/HA/HP
        :type  th:      :class:`string`
        :param rh:      resistencia                  20-50
        :type  rh:      :class:`int`
        :param ch:      consistencia                 S/P/B/F/L
        :type  ch:      :class:`string`
        :param tmh:     tamaño del árido             
        :type  tmh:     :class:`int`
        :param ah:      clase ambiente               I/IIa/IIb/IIIa/IIIb/IIIc
        :type  ah:      :class:`string`
        :param dn:      denominacion                
        :type  dn:      :class:`string`

        :param metodo:  metodo                
        :type  metodo:  :class:`string`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param pcem:    precio del cemento
        :type  pcem:    :class:`float`
        :param pare:    precio de la arena
        :type  pare:    :class:`float`
        :param pgra:    precio de la grava
        :type  pgra:    :class:`float`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param dcem:    dosificacion del cemento
        :type  dcem:    :class:`float`
        :param dare:    dosificacion de la arena
        :type  dare:    :class:`float`
        :param dgra:    dosificacion de la grava
        :type  dgra:    :class:`float`

        """
        self.th=th
        self.rh=rh
        self.ch=ch
        self.tmh=tmh
        self.ah=ah
        self.dn=dn
        self.metodo=metodo
        self.fecha=fecha
        self.pcem=pcem
        self.pare=pare
        self.pgrav=pgrav
        self.dcem=dcem
        self.dare=dare
        self.dgrav=dgrav
        self.dosificacion=str(dcem) + "/" + str(pcem) + "/"+ str(dare) + "/"+ str(pare) + "/" + str(dgrav) + "/" + str(pgrav)
        precio = round(pcem*dcem + pare*dare + pgrav*dgrav,2)
        self.precio = precio

    def dname_h(self):
        """
        Metodo para crear la designacion de los hormigones - HA - 30/P/20/I
        
        """
        dname_h = f'{self.th} - {self.rh}/{self.ch}/{self.tmh}/{self.ah}'
        return dname_h

    def dprecio_m(self):
        """
        Metodo para crear el precio descompuesto de los horigones a partir de los precios del cemento, arena y grava.
        
        """
        dprecio_m = self.pcem*self.dcem + self.pare*self.dare+self.pgrav*self.dgrav
        return dprecio_m



#horm_1   = hormigon_h("HA",30,"P",20,"I", "Hormigon Armado","Central",65.22,"2020-06-22","1")
#d_horm_1 = horm_1.dname_h()
#print(d_horm_1)


#horm_2   = hormigon_hd("HA",30,"B",40,"IIa", "Hormigon Armado","Obra","2020-06-22",113.19,21.2,11.2,0.17,0.42,0.85)
#d_horm_2 = horm_2.dname_h()
#p_horm_2 = horm_2.dprecio_m()
#print(d_horm_2)
#print(p_horm_2)