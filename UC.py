from reproducao_audio import *
from assistente import Assistente, Estado

if __name__ == '__main__':
    HOT_WORDS = ['Maiara', 'Mayara', 'Nayara']

    mayara = Assistente()
    while True:
        """ Primeiro estado onde a Assistente Virtual (AV) espera ser chamado pela "hot word". Quando acionado, 
        dira "bom dia"
        """
        if mayara.estado == Estado.ESPERA:
            if mayara.aguarda_fala(HOT_WORDS) is not None:
                mayara.reproduz_fala(Audio.BOM_DIA)
                mayara.avanca_estado()
        """ AV faz a leitura dos objetos a sua frente, e diz quais objetos ela viu."
        """
        if mayara.estado == Estado.LEITURA:
            if mayara.procura_objetos():
                mayara.fala_objetos_vistos()
                mayara.avanca_estado()
        """ AV aguarda usuario dizer qual objeto esta procurando.
        """
        if mayara.estado == Estado.AGUARDA_OBJETO:
            objetos_vistos = mayara.retorna_objetos_vistos()
            while mayara.objeto_em_mira is None:
                mayara.reproduz_fala(Audio.QUAL_DESEJA)
                texto_objeto = mayara.aguarda_fala(objetos_vistos)
                mayara.foca_em_objeto(texto_objeto)
            mayara.avanca_estado()
        """ AV vai orientar a mao do usuario a sobrepor o objeto buscado.
        """
        if mayara.estado == Estado.ORIENTACAO:
            while not mayara.direciona():
                pass
            mayara.avanca_estado()
        """ AV diz a mensagem de sucesso quando o objeto eh encontrado
        """
        if mayara.estado == Estado.OBJETO_ENCONTRADO:
            mayara.reproduz_fala(Audio.OBJETO_EM_MIRA)
            mayara.volta_para_estado_inicial()
            mayara.objeto_em_mira = None

