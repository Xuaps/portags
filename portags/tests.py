import models
import unittest

class TagTestCase(unittest.TestCase):
    def test_puedo_crear_un_tag(self):
        tag=models.Tag(nombre="juas")

        self.assertIsNotNone(tag)
        self.assertEqual(0,tag.numero_busquedas)

    def test_puedo_incrementar_el_numero_de_busuqedas(self):
        tag=models.Tag(nombre="juas")
        self.assertEqual(0,tag.numero_busquedas)

        tag.IncrementarNumeroBusquedas()

        self.assertEqual(1,tag.numero_busquedas)

class TagsFactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.tags=models.TagsFactory().BuildTagsFromString("juas tachan")

    def test_dada_una_busqueda_con_dos_tags_separados_por_espacio_puedo_obtener_dos_tags(self):
        self.failUnlessEqual(self.tags[0].nombre, "juas")
        self.failUnlessEqual(self.tags[1].nombre, "tachan")

    def test_dada_una_busqueda_con_dos_tags_separados_por_espacio_puedo_obtener_dos_tags_relacionados(self):
        self.failUnlessEqual(self.tags[0].tags_relacionados.all()[0], self.tags[1])
        self.failUnlessEqual(self.tags[1].tags_relacionados.all()[0], self.tags[0])

    def test_dada_una_busqueda_con_dos_tags_separados_por_espacio_puedo_obtener_dos_tags_relacionados_de_la_bd(self):
        tags=models.Tag.objects.all()
        self.failUnlessEqual(tags[0].tags_relacionados.all()[0], self.tags[1])
        self.failUnlessEqual(tags[1].tags_relacionados.all()[0], self.tags[0])

    def test_dada_una_busqueda_con_dos_tags_separados_por_espacio_cuando_busco_por_uno_de_ellos_puedo_obtener_sus_relacionados(self):
        tags=models.TagsFactory().BuildTagsFromString("juas")

        self.assertIsNotNone(tags[0].tags_relacionados)
        self.assertEqual(1,len(tags[0].tags_relacionados.all()))
        self.assertEqual('tachan', tags[0].tags_relacionados.all()[0].nombre)

    def test_dada_una_busqueda_con_tags_nuevos_el_numero_de_busquedas_es_igual_a_0(self):
        self.assertEqual("juas",self.tags[0].nombre)
        self.assertEqual(self.tags[0].numero_busquedas,0)


    def test_dada_una_busqueda_con_un_tag_existente_lo_recupera(self):
        tag=models.Tag.objects.get(nombre="juas")

        tags=models.TagsFactory().BuildTagsFromString("juas")

        self.assertEquals(tags[0].id,tag.id)

class HtmlFontSizerTestCase(unittest.TestCase):
    def setUp(self):
        self.tag=models.Tag(nombre="juas")
        self.sizer=models.HtmlFontSizer(50)

    def test_dado_un_tamanho_un_min_y_un_max_puedo_pasarlo_a_la_escala_de_fuentes(self):
        valor=self.sizer.calculateProporcionalValue(10)
        self.assertEqual(valor,1)

    def test_dado_un_tag_un_max_y_un_min_puedo_establecer_su_tamanho_a_xxsmall(self):
        self.sizer.setSizeTo(self.tag,2)

        self.assertEqual('xx-small',self.tag.size)

    def test_dado_un_tag_un_max_y_un_min_puedo_establecer_su_tamanho_a_xsmall(self):
        self.sizer.setSizeTo(self.tag,10)

        self.assertEqual('x-small',self.tag.size)

    def test_dado_un_tag_puedo_establecer_su_tamanho_a_small(self):
        self.sizer.setSizeTo(self.tag,15)

        self.assertEqual('small',self.tag.size)

    def test_dado_un_tag_puedo_establecer_su_tamanho_a_medium(self):
        self.sizer.setSizeTo(self.tag,27)

        self.assertEqual('medium',self.tag.size)

    def test_dado_un_tag_puedo_establecer_su_tamanho_a_large(self):
        self.sizer.setSizeTo(self.tag,35)

        self.assertEqual('large',self.tag.size)

    def test_dado_un_tag_puedo_establecer_su_tamanho_a_xlarge(self):
        self.sizer.setSizeTo(self.tag,42)

        self.assertEqual('x-large',self.tag.size)

    def test_dado_un_tag_puedo_establecer_su_tamanho_a_xxlarge(self):
        self.sizer.setSizeTo(self.tag,50)

        self.assertEqual('xx-large',self.tag.size)
