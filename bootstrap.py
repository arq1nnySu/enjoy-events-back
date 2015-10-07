from model.event import Event
from model.user import User
from model.visibility import Visibility


def remove(object):
	object.remove()

def development():
	map(remove, User.query.all())
	map(remove, Visibility.query.all())
	map(remove, Event.query.all())

	cpi = User(username='cpi', password='unq')
	cpi.save()

	arq1 = User(username='arq1', password='lds')
	arq1.save()

	public = Visibility(name='Public')
	public.save()


	private = Visibility(name='Private')
	private.save()

	event = Event(
	    date= 'Thu Sep 24 2015 17=24=10 GMT-0300 (ART)',
	    description= "\t\t\t\t\t\t\t\t\t        <h3 style=\"font-weight:bold; color:rgba(205,0,3,1.00)\">Lollapalooza<\/h3>                  <ul>            <li>Se podrán comprar las entradas con un beneficio de hasta 6 cuotas sin interés durante todo el periodo de venta.<\/li>         <\/ul>           <p>&nbsp;<\/p> <div class=\"tab-pane active\" id=\"primero\">             <h2 style=\" color:#6c3c91\">Lollapalooza<\/h2>             <p><strong>Lollapalooza<\/strong>&nbsp;se caracteriza por presentar a las bandas más importantes y vanguardistas de la escena internacional y nacional. Algunas de las que ya formaron parte son:&nbsp;<strong>Red Hot Chilli Peppers, Jack White, Arcade Fire, Pharrell Williams, Calvin Harris, Nine Inch Nails, Robert Plant and the Sensantional Space Shifter, Phoenix, Soundgarden, Pixies, Skrillex, The Smashing Pumpkins, Foster The People, Kasabian, The Kooks, Cypress Hill, Interpol, Axwell, Vampire Weekend, Alt-J, New Order, Julian Casablancas, Ellie Goulding, Lorde, Imagine Dragons, Bastille, Major Lazer, Johnny Marr, Jake Bugg, Capital Cities, Chet Faker, IKV, Pedro Aznar, Juana Molina, Onda Vaga, Pez y muchas bandas más.<\/strong><\/p>             <p><strong>Lollapalooza<\/strong>&nbsp;es una experiencia única y sin antecedentes en nuestro país, donde más de&nbsp;<strong>50 bandas internacionales y nacionales<\/strong>&nbsp;se presentan a lo largo de&nbsp;<strong>2 días<\/strong>&nbsp;en los&nbsp;<strong>5 escenarios<\/strong>&nbsp;distribuidos en el Hipódromo de San Isidro, un predio especialmente acondicionado para esta inmensa&nbsp;<strong>experiencia<\/strong>&nbsp;de <strong>música y arte<\/strong>, sumados a una amplia propuesta&nbsp;<strong>gastronómica<\/strong>&nbsp;con más de&nbsp;<strong>30 opciones<\/strong>&nbsp;para todos los gustos.<\/p>             <p>Para los amantes de la indumentaria, todos los años Lollapalooza sorprende con una gran colección de<strong> Merchandising<\/strong>&nbsp;con nuevos diseños exclusivos de ropa y accesorios.<\/p>             <p>Los más pequeños también tienen su lugar dentro de&nbsp;<strong>Lollapalooza: Kidzapalooza<\/strong>. Un espacio creado exclusivamente para la diversión y la seguridad de los más chicos. El escenario Kidzapalooza cuenta con reconocidas bandas para el público infantil, talleres recreativos para los chicos y sus familias. Durante los dos días el espacio al aire libre pensado para los más pequeños y sus familias, se convierte en un espacio mágico en donde todos pueden vivir experiencias únicas e inolvidables. Los chicos&nbsp;<strong>hasta 10 años pueden ingresar en forma gratuita<\/strong>&nbsp;al festival acompañados de un adulto con entrada.<\/p>             <p>Los chicos que hayan cumplido 11 años deberán comprar su entrada de ingreso al festival.<\/p>             <p>Otro de los espacios que se destacan en este festival es&nbsp;<strong>Espíritu Verde<\/strong>; un lugar para concientizar el cuidado del medio ambiente. Espiritu verde promueve el desarrollo sustentable, tanto desde lo ambiental como desde lo social, contando con el apoyo institucional de la ONU \u2013 Naciones Unidas Argentina.<\/p>             <p><strong>ROCK &amp; RECYCLE<\/strong>&nbsp;busca reducir al mínimo la huella ambiental del evento a través de la separación en origen de los residuos generados durante<\/p>           <\/div>          \t\t\t\t\t\t\t\t",
	    image= 'http://static.passto.com.ar.s3.amazonaws.com/lollapalooza/lolla-banner-nuevo.jpg',
	    name= 'Lollapalooza 2016',
	    tag= 'LollaAR',
	    time= '10:00',
	    venue= 'Hipodromo de san isidro',
		owner = cpi,
		visibility = public,
		gests = []
	)

	event.save()

	event2 = Event(
	    date= 'Thu Sep 24 2015 17=24=10 GMT-0300 (ART)',
	    description= 'Choripateada de TPI',
	    image= 'http://www.pasqualinonet.com.ar/images/Chorizos-765w%20007b.jpg',
	    name= 'Choripateada 2015',
	    tag= 'chori_2015',
	    time= '10:00',
	    venue= 'Universidad Nacional de Quilmes (UNQ)',
		owner = cpi,
		visibility = private,
		gests = [arq1]
	)

	event2.save()



if __name__ == '__main__':
	development()


