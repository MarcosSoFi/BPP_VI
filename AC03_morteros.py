
# Clase Morteros

class mortero_m:
    """
    Según la UNE - EN 998 - 2
    Morteros para  para albañileria
    
    >>> m_1  = mortero_m("M",5,"Mortero Gris","Sacos",127.24,"2020-06-22","1")
    >>> d_m_1 = m_1.dname_m()
    >>> print(d_m_1)
    >>> M - 5

    """
    def __init__(self,tpm,rm,dn,metodo,precio,fecha,dosificacion):
        """
        Constructor de la clase Morteros

        :param tpm:     tipo de mortero             M
        :type  tpm:     :class:`string`       
        :param rm:      resistencia del mortero     1/2.5/5/7.5/10
        :type  rm:      :class:`string`
        :param dn:      designación                 
        :type  dn:      :class:`string`
        :param metodo:  metodo de distribucion      
        :type  metodo:  :class:`string`

        :param precio:  precio  
        :type  precio:  :class:`float`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param dosificacion:   fecha  
        :type  dosificacion:  :class:`string``

        """
        self.tpm=tpm
        self.rm=rm
        self.dn=dn
        self.metodo=metodo
        self.precio=precio
        self.fecha=fecha
        self.dosificacion=dosificacion

    def dname_m(self):
        """
        Metodo para crear la designacion de los morteros
        
        """
        dname_m=f'{self.tpm} - {self.rm}'
        return dname_m
    

#m_1  = mortero_m("M",5,"Mortero Gris","Sacos",127.24,"2020-06-22","1")
#d_m_1 = m_1.dname_m()
#print(d_m_1)