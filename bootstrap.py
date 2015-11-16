# coding=utf-8
from model.event import Event, Venue
from model.user import User
from model.assistance import Assistance, Requirement, AssistanceEvent
from model.visibility import Visibility
from datetime import date, timedelta


def remove(object):
    object.remove()


def development():
    map(remove, User.query.all())
    map(remove, Visibility.query.all())
    map(remove, Assistance.query.all())
    map(remove, Event.query.all())
    map(remove, Requirement.query.all())
    map(remove, Venue.query.all())

    cpi = User(username='cpi', password='unq', email="cpi@unq.edu.ar", firstName="CPI", lastName="UNQ", phone="123456")
    cpi.generate_hashed_password()
    cpi.save()

    arq1 = User(username='arq1', password='lds', email="arq1@unq.edu.ar", firstName="ARQ1", lastName="UNQ", phone="123456")
    arq1.generate_hashed_password()
    arq1.save()

    nny = User(username='nnydjesus', password='123', email="nnydjesus@gmail.com", firstName="Ronny", lastName="De Jesus", phone="123456")
    nny.generate_hashed_password()
    nny.save()


    public = Visibility(name='Public')
    public.save()

    private = Visibility(name='Private')
    private.save()

    hipodromo = Venue(name="Hipodromo de san isidro", street="Av. Marquez 504", city="San Isidro", country="Argentina")
    hipodromo.save()

    event = Event(
        date=date.today().strftime('%Y-%m-%d'),
        description="\t\t\t\t\t\t\t\t\t        <h3 style='font-weight:bold; color:rgba(205,0,3,1.00)'>Lollapalooza</h3>                  <ul>            <li>Se podran comprar las entradas con un beneficio de hasta 6 cuotas sin interes durante todo el periodo de venta.</li>         </ul>           <p>&nbsp;</p> <div class='tab-pane active' id='primero'>             <h2 style=' color:#6c3c91'>Lollapalooza</h2>             <p><strong>Lollapalooza</strong>&nbsp;se caracteriza por presentar a las bandas mas importantes y vanguardistas de la escena internacional y nacional. Algunas de las que ya formaron parte son:&nbsp;<strong>Red Hot Chilli Peppers, Jack White, Arcade Fire, Pharrell Williams, Calvin Harris, Nine Inch Nails, Robert Plant and the Sensantional Space Shifter, Phoenix, Soundgarden, Pixies, Skrillex, The Smashing Pumpkins, Foster The People, Kasabian, The Kooks, Cypress Hill, Interpol, Axwell, Vampire Weekend, Alt-J, New Order, Julian Casablancas, Ellie Goulding, Lorde, Imagine Dragons, Bastille, Major Lazer, Johnny Marr, Jake Bugg, Capital Cities, Chet Faker, IKV, Pedro Aznar, Juana Molina, Onda Vaga, Pez y muchas bandas mas.</strong></p>             <p><strong>Lollapalooza</strong>&nbsp;es una experiencia unica y sin antecedentes en nuestro pais, donde mas de&nbsp;<strong>50 bandas internacionales y nacionales</strong>&nbsp;se presentan a lo largo de&nbsp;<strong>2 dias</strong>&nbsp;en los&nbsp;<strong>5 escenarios</strong>&nbsp;distribuidos en el Hipodromo de San Isidro, un predio especialmente acondicionado para esta inmensa&nbsp;<strong>experiencia</strong>&nbsp;de <strong>musica y arte</strong>, sumados a una amplia propuesta&nbsp;<strong>gastronomica</strong>&nbsp;con mas de&nbsp;<strong>30 opciones</strong>&nbsp;para todos los gustos.</p>             <p>Para los amantes de la indumentaria, todos los anos Lollapalooza sorprende con una gran coleccion de<strong> Merchandising</strong>&nbsp;con nuevos disenos exclusivos de ropa y accesorios.</p>             <p>Los mas pequenos tambien tienen su lugar dentro de&nbsp;<strong>Lollapalooza: Kidzapalooza</strong>. Un espacio creado exclusivamente para la diversion y la seguridad de los mas chicos. El escenario Kidzapalooza cuenta con reconocidas bandas para el publico infantil, talleres recreativos para los chicos y sus familias. Durante los dos dias el espacio al aire libre pensado para los mas pequenos y sus familias, se convierte en un espacio magico en donde todos pueden vivir experiencias unicas e inolvidables. Los chicos&nbsp;<strong>hasta 10 anos pueden ingresar en forma gratuita</strong>&nbsp;al festival acompanados de un adulto con entrada.</p>             <p>Los chicos que hayan cumplido 11 anos deberan comprar su entrada de ingreso al festival.</p>             <p>Otro de los espacios que se destacan en este festival es&nbsp;<strong>Espiritu Verde</strong>; un lugar para concientizar el cuidado del medio ambiente. Espiritu verde promueve el desarrollo sustentable, tanto desde lo ambiental como desde lo social, contando con el apoyo institucional de la ONU \u2013 Naciones Unidas Argentina.</p>             <p><strong>ROCK &amp; RECYCLE</strong>&nbsp;busca reducir al minimo la huella ambiental del evento a traves de la separacion en origen de los residuos generados durante</p>           </div>          \t\t\t\t\t\t\t\t",
        image='http://static.passto.com.ar.s3.amazonaws.com/lollapalooza/lolla-banner-nuevo.jpg',
        name='Lollapalooza 2016',
        tag='LollaAR',
        time='10:00',
        venue= hipodromo,
        owner=nny,
        visibility=public,
        gests=[],
        requirement = [Requirement(name='Sandwich de milanesa', quantity=5),Requirement(name='Gaseosas',quantity=10)],
        capacity = 10
    )

    event.save()



    assistanceEvent1 = AssistanceEvent(tag=event.tag, name=event.name, venue=event.venue.name, date=event.date, 
            time=event.time, image=event.image)

    assistance1 = Assistance(
        eventTag = assistanceEvent1.tag,
        event = assistanceEvent1,
        user = cpi.username,
        requirements = [Requirement(name='Sandwich de milanesa',quantity=3),Requirement(name='Gaseosas',quantity=1)]
        )

    # assistance1.save()

    assistance2 = Assistance(
        eventTag = assistanceEvent1.tag,
        event = assistanceEvent1,
        user = arq1.username,
        requirements = [Requirement(name='Sandwich de milanesa',quantity=2),Requirement(name='Gaseosas',quantity=1)]
        )
    # assistance2.save()


    unq = Venue(name="Universidad Nacional de Quilmes (UNQ)", street="Roque Saenz Pena 352", city="Bernal", country="Argentina")
    unq.save()
    event2 = Event(
        date=(date.today() + timedelta(days=17)).strftime('%Y-%m-%d'),
        description='Choripateada de TPI',
        image='http://www.pasqualinonet.com.ar/images/Chorizos-765w%20007b.jpg',
        name='Choripateada 2015',
        tag='chori_2015',
        time='10:00',
        venue=unq,
        owner=cpi,
        visibility=private,
        gests=[nny.username],
        requirement = [Requirement(name='Provoleta',quantity=5),Requirement(name='Alfajores Capitan del Espacio',quantity=10)],
        capacity = 5
    )

    event2.addGest(arq1)

    event2.save()

    assistanceEvent2 = AssistanceEvent(tag=event2.tag, name=event2.name, venue=event2.venue.name, date=event2.date, 
            time=event2.time, image=event2.image)
    assistance3 = Assistance(
        eventTag = assistanceEvent2.tag,
        event = assistanceEvent2,
        user = cpi.username,
        requirements = [Requirement(name='Provoleta',quantity=1)]
        )
    
    assistance3.save()

    assistance4 = Assistance(
        eventTag = assistanceEvent2.tag,
        event = assistanceEvent2,
        user = arq1.username,
        requirements = [Requirement(name='Alfajores Capitan del Espacio',quantity=3),Requirement(name='Provoleta',quantity=2)]
        )

    assistance4.save()

    galvez = Venue(name="Predio Vieja Iglesia de Galvez", street="Nazareno Rossi y Santiago de Liniers", city="Santa Fe", country="Argentina")
    galvez.save()

    event4= Event(
        date=(date.today() + timedelta(days=5)).strftime('%Y-%m-%d'),
        description='<div class="col-md-1">&nbsp;</div><div class="col-xs-10"><h1 style="text-align:center"><strong>#NosDisfrazamosTodos #NDT</strong></h1><h4 style="text-align:center"><span style="font-size:20px">La Fiesta de Disfraces + Grande de la zona y la + copada Provincia de Santa Fe en su 6ta Edici&oacute;n</span></h4><hr /><h4 style="text-align:center">3 PISTAS</h4><p style="text-align:center">&gt;&gt; Pista Central FIESTA &gt;&gt; Performance &gt;&gt; Live Show<br />Carpa Electr&oacute;nica [[[[]]]]<br />[[ Pista 80&acute;90&acute;00&acute; ]]</p><hr /><h4 style="text-align:center">SPONSORS</h4><p style="text-align:center">|| Cablenet Nplay || On Club || Pico Dulce ||</p><hr /><p style="text-align:center">|| Patio de Comidas || Estacionamiento Privado || Sector Living Fun || Juegos || Sector Fotos || Confesionario ||</p><hr /><iframe frameborder="0" height="350" src="https://www.youtube.com/embed/lSYZLBtwhFA" width="100%"></iframe></div><div class="col-md-1">&nbsp;</div>',
        image='http://static.passto.com.ar/images/1446217982549-297-image-cover3.jpg',
        name='Nos Disfrazamos Todos',
        tag='NDT',
        time='10:00',
        venue= galvez,
        owner=cpi,
        visibility=public,
        gests=[],
        requirement = [],
        capacity = 100
    )

    event4.save()

    galvez = Venue(name="Sheraton Mendoza", street="Primitivo de la Reta 1009", city="Mendoza", country="Argentina")
    galvez.save()


    event5= Event(
        date=(date.today() + timedelta(days=14)).strftime('%Y-%m-%d'),
        description='<div class="col-xs-12"><h1 style="text-align:center"><strong>FALSA BODA</strong><br /><strong>Mendoza</strong><br /><span style="font-size:22px">#FalsaBoda</span></h1><h4 style="text-align:center">28 de noviembre</h4><hr /><p style="text-align:justify">Toda la exclusividad de la Fiesta M&aacute;s Divertida del Mundo, potencia su originalidad en la ciudad del vino.</p><p style="text-align:justify">El Hotel Sheraton Mendoza ser&aacute; el flamante anfitri&oacute;n de la primer Falsa Boda celebrada en su ciudad, explotando al m&aacute;ximo todo la excelencia y est&eacute;tica de este peculiar evento y haciendo del 28 de Noviembre una noche inolvidable.</p><p style="text-align:justify">Falsa Boda es un evento exclusivo para aquellas personas que poseen el deseo de ir a una boda, vestirse de gala, asistir con amigos, y disfrutar de la energ&iacute;a que se transmite en este tipo de eventos.</p><p style="text-align:justify">Ya no ten&eacute;s que esperar a que un amigo tome la decisi&oacute;n, ahora podes ser parte de una Falsa Boda.</p><p style="text-align:justify">Este es un evento donde se respetan muchos de los t&iacute;picos rituales (sin duda los m&aacute;s divertidos): novios, ceremonia, vestimenta elegante, ramo, baile, barra libre, shows, recepci&oacute;n, postre y final de fiesta, comenzando la noche en la parte m&aacute;s divertida de este tipo de eventos, aquella que se da despu&eacute;s de las 23.00 hs.</p><hr /><p style="text-align:justify">Es condici&oacute;n obligatoria:</p><ul><li>Asistir de GALA</li><li>Ingresar entre las 23:00 y 00:00 a.m.</li><li>Ser mayor de 23 a&ntilde;os.</li></ul><p>El servicio incluye ingreso, barra libre y bandejeo gourmet.</p><p style="text-align:justify">Las invitaciones NO se retiran. Al adquirirlas recibir&aacute;s un c&oacute;digo QR. El mismo sirve como comprobante para ingresar al evento, impreso o desde tu celular.<br />La &uacute;nica diferencia entre un precio y otro es la fecha en que se compran, todos acceden al mismo sector de la fiesta y cuentan con los mismos servicios.</p><p style="text-align:justify">Los esperamos para vivir una gran experiencia!<br />Vos podes ser parte de La Fiesta Mas Divertida Del Mundo</p><hr /><iframe frameborder="0" height="350" src="https://player.vimeo.com/video/140616376" width="100%"></iframe></div>',
        image='http://static.passto.com.ar/images/1445953367077-337-image-cover3.jpg',
        name='FALSA BODA Mendoza',
        tag='FalsaBodaM',
        time='10:00',
        venue= galvez,
        owner=cpi,
        visibility=public,
        gests=[],
        requirement = [],
        capacity = 100
    )

    event5.save()


    laPlata = Venue(name="Estadio Unico La Plata", street="Av. 25, 1900", city="La Plata", country="Argentina")
    laPlata.save()


    event6= Event(
        date=(date.today() + timedelta(days=20)).strftime('%Y-%m-%d'),
        description='<div class="cuerposmart clearfix"><div style="display:block;"><p>Los <b><a href="http://www.infobae.com/rolling-stones-a894" class="agrupador" rel="894">Rolling Stones</a> </b>se presentaran el domingo <b>7 de febrero</b> en el Estadio Unico de la ciudad de La Plata, segun pudo saber <b>Infobae</b>. Ademas, la banda, integrada por Mick Jagger, Keith Richards, Charlie Watts y Ronnie Wood, dara otros dos recitales el <b>miercoles 10 y el sabado 13</b>.  </p>  <p>Esta es la primera vez que tocaran en La Plata. En las visitas anteriores, realizaron 12 shows en el Estadio de River Plate. La primera vez que tocaron en nuestro pais fue en 1998, la segunda en 1998 y la ultima en 2006.</p>  <p>No fueron<a href="http://www.infobae.com/2015/09/22/1757197-el-dolar-factor-clave-concretar-la-visita-los-rolling-stones-la-argentina"> faciles las negociaciones</a> para traer a los Stones a la Argentina. <b>Daniel Grinbank</b>, productor de espectaculos que estuvo involucrado en los shows anteriores en el pais, reconocio que fue un tema complejo:<b> "Sobre todo por las circunstancias, no solo en la Argentina, que vive la region, donde la moneda local se ha devaluado frente al dolar, mas que en otras regiones".</b></p><div class="embed_cont type_freetext" rel="freetext" id="embed30_wrap" onmousedown="return false;"><div class="embed_options" rel="opt" id="embed30_opts" onmousedown="return false;"><span id="embed30_colapse" class="embed_colapse less">     </span> Embed</div><div id="embed30_content" class="embed_content"><div id="embed30_embed"><iframe width="770" height="433" src="https://www.youtube.com/embed/H63rznBjt9w" frameborder="0" allowfullscreen=""></iframe></div></div><div ></div><div ></div></div><p>Este ano, los Rolling Stones estuvieron presentando su <i>Zip Code Tour</i> por distintas ciudades de los Estados Unidos. Ahora los fanaticos solo deberan esperar hasta febrero de 2016 cuando ellos visiten nuestro pais, como parte de su gira por Sudamerica. </p> <p></p></div> </div>',
        image='http://ciudad.cdncmd.com/sites/default/files/styles/ciu_nota_slider_contenido_hd/public/nota/2015/10/08/rolling_stones_2016_argentina.jpg?itok=6i7RzjHB',
        name='The Rolling Stones 2016',
        tag='TRS2016',
        time='10:00',
        venue= laPlata,
        owner=cpi,
        visibility=public,
        gests=[],
        requirement = [],
        capacity = 100
    )

    event6.save()


if __name__ == '__main__':
    development()
    # evento = Event.query.get_by_tag("LollaAR")
    # evento.lackRequirements() 
