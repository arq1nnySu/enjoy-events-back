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
        owner=cpi,
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
        gests=[],
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


if __name__ == '__main__':
    development()
    # evento = Event.query.get_by_tag("LollaAR")
    # evento.lackRequirements() 
