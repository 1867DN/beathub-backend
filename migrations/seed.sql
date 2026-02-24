-- BeatHub - Seed Data SQL
-- Generado desde DB local
-- Uso: psql -U postgres -d <dbname> -f seed.sql

-- Desactivar restricciones FK temporalmente
SET session_replication_role = replica;

TRUNCATE TABLE products, categories, brands RESTART IDENTITY CASCADE;

-- Brands
INSERT INTO brands (id_key, name, logo_path) VALUES (1, 'AMT', 'amt.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (2, 'AMUMU STRAPS', 'amumu_straps.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (3, 'ANLEON', 'anleon.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (4, 'ALTO PROFESSIONAL', 'alto_professional.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (5, 'BARE KNUCKLE', 'bare_knuckle.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (6, 'CHAPMAN GUITARS', 'chapman_guitars.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (7, 'CLAYTON', 'clayton.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (8, 'DARKGLASS', 'darkglass.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (9, 'DEMONFX', 'demonfx.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (10, 'DSM HUMBOLDT', 'dsm_humboldt.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (11, 'FLANGER', 'flanger.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (12, 'FLAMMA', 'flamma.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (13, 'GRUVGEAR', 'gruvgear.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (14, 'HEADRUSH', 'headrush.png');
INSERT INTO brands (id_key, name, logo_path) VALUES (15, 'SPIRA GUITARS', 'spira_guitars.png');

-- Categories
INSERT INTO categories (id_key, name) VALUES (7, 'Emulador de Amplificador');
INSERT INTO categories (id_key, name) VALUES (8, 'Correas');
INSERT INTO categories (id_key, name) VALUES (9, 'Monitores Personales');
INSERT INTO categories (id_key, name) VALUES (10, 'Sistemas Inalámbricos In-Ear');
INSERT INTO categories (id_key, name) VALUES (11, 'Mixers');
INSERT INTO categories (id_key, name) VALUES (12, 'Micrófonos Inalámbricos');
INSERT INTO categories (id_key, name) VALUES (13, 'Subwoofers');
INSERT INTO categories (id_key, name) VALUES (14, 'Altavoz Portátil');
INSERT INTO categories (id_key, name) VALUES (15, 'Pastillas Humbucker');
INSERT INTO categories (id_key, name) VALUES (16, 'Guitarras Eléctricas');
INSERT INTO categories (id_key, name) VALUES (17, 'Púas');
INSERT INTO categories (id_key, name) VALUES (18, 'Pedalera para bajo');
INSERT INTO categories (id_key, name) VALUES (19, 'Pedal para bajo y guitarra');
INSERT INTO categories (id_key, name) VALUES (20, 'Amplificador para bajo');
INSERT INTO categories (id_key, name) VALUES (21, 'Potenciometros');
INSERT INTO categories (id_key, name) VALUES (22, 'Cabezal para bajo');
INSERT INTO categories (id_key, name) VALUES (23, 'Preamplificador para guitarra');
INSERT INTO categories (id_key, name) VALUES (24, 'Preamplificador para bajo');
INSERT INTO categories (id_key, name) VALUES (25, 'Pedalera para guitarra');
INSERT INTO categories (id_key, name) VALUES (26, 'Afinadores');
INSERT INTO categories (id_key, name) VALUES (27, 'Pedal para guitarra eléctrica');
INSERT INTO categories (id_key, name) VALUES (28, 'Consola digital');
INSERT INTO categories (id_key, name) VALUES (32, 'Soporte para instrumentos');
INSERT INTO categories (id_key, name) VALUES (33, 'Accesorio para instrumentos');
INSERT INTO categories (id_key, name) VALUES (34, 'Pedalera looper');
INSERT INTO categories (id_key, name) VALUES (35, 'Parlante potenciado');

-- Products
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (11, 'Pedal Legend Amps Amt F1 Twin Emulates Guitarra MINT', 178056.0, 197840.0, 9, 'AMT F-1 LEGEND AMPS
El F-1 fue uno de los primeros diseños de la serie Legend Amps, diseñado para lograr el clásico sonido de un Fender Twin. Se puede usar para crear un preamp multi canal desde canales mono de cualquiera de los pedales de la serie Legend Amps (P-1, B-1, M-1, R-1, S-1). Así la serie se expande constantemente, ofreciendo la oportunidad de lograr un sonido 100% análogo para tu guitarra.

Este pedal es un preamp con un canal limpio interno y la posibilidad de alternarlo con un canal externo (cualquier otro pedal de overdrive). Posee un loop de efectos con una entrada estándar de -10dB preparada para enchufar cualquier efecto auxiliar y boostearlo a 0dB o más, lo cual es más que suficiente para operar directamente con la potencia del amplificador. En caso de conectar a una mixer o computadora, el preamp tiene simulador de caja y parlantes.', 1, 'amt/2pedal_legend_amps_amt_f1_twin_emulates_guitarra_mint.png', 'true', 'false', 'false', 7, 1);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (12, 'Pedal Amt E Drive Ed2 Emulador Engl Para Guitarra MINT', 109147.5, 121275.0, 0, 'El E-Drive fue diseñado para guitarristas que buscan una distorsión similar a la de los amplificadores ENGL. La serie de efectos Drive fue diseñada para ser conectada en el canal clean de un equipo, por lo cual no emula cajas ni parlantes como los de la serie Legend Amp. Estos pedales permiten al guitarrista obtener un cálido y crujiente sonido, emulando el sonido de los clásicos amplificadores valvulares pero preservando la esencia del tono del instrumento y amplificador utilizados.', 6, 'amt/pedal_amt_e_drive_ed2_emulador_engl_para_guitarra_mint.png', 'true', 'false', 'false', 7, 1);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (13, 'Pedal Amt Ss20 Preamplificador Valvular Para Guitarra *USADO*', 315000.0, 350000.0, 12, 'Las características de SS-20: Alimentación de triodos de alto voltaje de alto grado. Eliminación completa de los amplificadores operacionales usados tradicionalmente en preamplificadores híbridos. Aplicación de amplificadores especiales de semiconductores que modelan armónicos basados en triodos y proporcionan la amplitud de señal necesaria para el funcionamiento de válvulas de alto grado. Las propiedades dinámicas características de los preamplificadores basados en válvulas se implementan en SS-20 con cascadas especiales capaces de alcanzar amplitudes de 250V con no linealidad similar a Triodo 12AX7.', 7, 'amt/pedal_amt_ss20_preamplificador_valvular_para_guitarra_usado.png', 'true', 'false', 'false', 7, 1);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (14, 'Pedal Amt Ss30 Bulava Jfet Preamplificador Para Guitarra *USADO*', 225000.0, 250000.0, 5, 'AMT SS-30 BULAVA (3-CHANNEL JFET GUITAR PREAMP). El SS-30 es un preamp de tres canales con poder de sobra. No posee válvulas sino transistores JFET, ofreciendo un tono high gain moderno, ideal para estilos metaleros. Posee tres canales con control de master independiente por canal e incluye loop de efectos. Tiene dos salidas: una para amplificador y otra de línea directa para consola, computadora o dispositivo de mezcla, ideal para grabar.', 3, 'amt/pedal_amt_ss30_bulava_jfet_preamplificador_para_guitarra_usado.png', 'true', 'false', 'false', 7, 1);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (15, 'Correa Amumu SNAPLOCK PRO Para Guitarra o Bajo VARIOS COLORES', 28378.8, 31532.0, 8, 'La correa de guitarra AMUMU SNAPLOCK Pro ofrece una seguridad y comodidad inigualables. Fabricada con cinta de seguridad de nailon de alta tenacidad de 2", brinda gran resistencia, durabilidad y resistencia al desgaste, ideal para movimientos dinámicos como saltos y giros de guitarra. Los casquillos reforzados y los tornillos extralargos garantizan un ajuste seguro en la mayoría de guitarras eléctricas y bajos sin necesidad de cuero. Los broches de presión Duraflex de alta resistencia permiten cambiar fácilmente de guitarra con solo presionar con la yema del dedo. Las hebillas adaptadoras de POM de alta resistencia garantizan que la correa soporte más de 54 kg (120 lbs). Los porta púas de acceso rápido patentados mantienen tus púas siempre al alcance.', 6, 'amumu_straps/correa_amumu_snaplock_pro_para_guitarra_o_bajo_varios_colores.png', 'true', 'false', 'false', 8, 2);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (16, 'Correa Amumu PC12P-BK Digital Dots Para Guitarra o Bajo', 22702.5, 25225.0, 0, 'Correa de Guitarra Amumu White Dots fabricada en poliéster algodón suave y resistente, con hebilla de plástico que evita rayones. Longitud ajustable de 36" a 62" (de agujero a agujero) para adaptarse a la medida más cómoda para vos. Compatible con guitarra acústica, guitarra eléctrica, bajo, mandolina y ukelele.', 9, 'amumu_straps/correa_amumu_pc12p-bk_digital_dots_para_guitarra_o_bajo.png', 'true', 'false', 'false', 8, 2);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (17, 'Correa Amumu CO35J Love Flower Para Guitarra o Bajo', 38651.4, 42946.0, 5, 'Correa para guitarra Amumu Love and Flower con extremos de cuero premium y una amplia longitud ajustable de 94 a 160 cm (de orificio a orificio), adecuada para la mayoría de los músicos. Su diseño de doble capa la hace más duradera y cómoda. La capa superior está hecha de poliéster con un patrón vintage tipo jacquard, mientras que la capa trasera está confeccionada en nailon suave. Si tu guitarra solo tiene un botón inferior para la correa, la cinta para el clavijero incluida te permitirá colocarla sin problemas.', 5, 'amumu_straps/correa_amumu_co35j_love_flower_para_guitarra_o_bajo.png', 'true', 'false', 'false', 8, 2);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (18, 'Correa Amumu Velvet Deluxe Para Guitarra o Bajo VARIOS COLORES', 43816.5, 48685.0, 3, 'Lleva la elegancia escénica y la máxima comodidad a tus presentaciones con la correa para guitarra AMUMU Velvet Deluxe Series. Esta versión mejorada incorpora un acolchado con patrón de diamante en lujoso terciopelo cristal, combinado con un reverso de algodón transpirable para un confort superior. Sus extremos de cuero genuino de primera calidad brindan resistencia y seguridad con el máximo agarre. Las costuras reforzadas y la hebilla metálica duradera aseguran tranquilidad tanto en el escenario como en el estudio. Fácilmente ajustable de 36" a 63", compatible con acústicas, eléctricas y bajos. Viene lista para regalar con bloques de goma de seguridad y correa de sujeción para la pala.', 2, 'amumu_straps/correa_amumu_velvet_deluxe_para_guitarra_o_bajo_varios_colores.png', 'true', 'false', 'false', 8, 2);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (19, 'Amplificador Para Monitoreo Personal Anleon Pm200 Stereo', 84368.7, 93743.0, 0, 'Anleon Pm200
El PM200 es un dispositivo de monitoreo personal con una entrada de línea TRS estéreo / mono de 1/4'''', una entrada de micrófono XLR única y un paso de XLR cableado, y una entrada de instrumento estéreo / mono de 1/4'''' con dos transformadores balanceados y salidas XLR aisladas. Las tres entradas también se enrutan a través de controles de nivel individuales, a una salida de teléfono de 1/4" y de 1/8" (3.5 mm).
Las salidas Mic Through e Instrument tienen elevadores de tierra puenteados para eliminar el zumbido de tierra. El PM200 es ideal para bandas en vivo y músicos de iglesia, así como músicos de estudio y cantantes.
Tener la capacidad de monitorear una mezcla principal junto con la voz del músico y su instrumento hace que el PM200 sea una herramienta eficaz y versátil.

Especificaciones: Nivel de entrada máximo: -20dB XLR, +40 dB de línea, +15dB Instrument. Impedancia de entrada: 50 kOhms. Respuesta de frecuencia de salida: 10 Hz - 30 kHz ± 3dB. Impedancia de salida, Auriculares: 10 ohmios. Impedancia de salida, Instrumento: 2 ea; balanceada 100 ohmios. Ganancia: 20 dB 1/4, 50 dB XLR. Respuesta de frecuencia de auriculares: 20 Hz - 20 kHz. Relación señal/ruido: 90 dB', 5, 'anleon/amplificador_para_monitoreo_personal_anleon_pm200_stereo.png', 'true', 'false', 'false', 9, 3);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (20, 'Sistema Inalambrico Anleon S2 Kit Para Monitoreo In Ear', 224113.99, 249015.54, 7, 'Anleon S2 Kit
ANLEON S2 es un sistema de monitorización in-ear (IEM) diseñado para actuaciones en escenario y transmisiones. Su alta relación señal/ruido y rango dinámico garantizan una calidad de audio óptima. Las dos entradas XLR duales permiten la operación de 2 canales, mono o estéreo, con una función de mezcla conveniente que te permite utilizar dos fuentes con el S2.

Características:
- 36 canales seleccionables
- Alimentado por 2 pilas alcalinas o pilas recargables (NiMH), no se recomiendan pilas de litio AA
- Varias series de receptores pueden funcionar con un solo transmisor dentro del rango de operación
- Circuito de expansión dinámica para una alta relación señal/ruido
- Circuito de anti-interferencia complejo para usar 3 conjuntos al mismo tiempo sin interferencias mutuas
- La pantalla LCD del receptor muestra la frecuencia, el canal y el nivel de batería
- Largo alcance de operación de hasta 100 metros

Cuando conectes el S2T transmisor a una mezcladora, ten cuidado con la cantidad de señal que envías. Si la señal de entrada es demasiado alta, la señal de salida del receptor se distorsionará y el sonido se cortará con frecuencia.', 3, 'anleon/sistema_inalambrico_anleon_s2_kit_para_monitoreo_in_ear.png', 'true', 'true', 'false', 10, 3);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (21, 'Mini Mixer Anleon Mx400 4 Canales Mono 5 Canales Stereo', 62653.5, 69615.0, 3, 'MX400 - Mezclador de línea mono de 4 canales y mezclador de audio estéreo de 5 canales.

Mezclador de línea mono de 4 canales: La función de mezclador de 4 canales es adecuada para mezclas de guitarras / bajos / teclados. Es perfecto para cualquiera que desee mezclar señales de 4 niveles de línea de forma rápida y sin complicaciones.

- Mezclador de línea mono ultracompacto de 4 canales para instrumentos
- La más alta calidad sonora incluso al nivel de salida máximo
- Control de nivel de entrada para cada canal
- Amplificadores operacionales de ruido ultrabajo para un rendimiento de audio excepcional

Mezclador estéreo de 5 canales: la unidad mezcla hasta cinco señales estéreo tales como CD / TV / teléfono / MP3 / Mac Mini / PS3 / Xbox / FM Tuner / Phono Player / Echo / Alexa / Chromecast y más.', 7, 'anleon/mini_mixer_anleon_mx400_4_canales_mono_5_canales_stereo.png', 'true', 'false', 'false', 11, 3);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (22, 'Sistema Anleon B1 Microfono Vocal Inalambrico Alcance 100 Metros', 383504.15, 426115.72, 11, 'Sistema Anleon B1 - Micrófono Vocal Inalámbrico
Este sistema inalámbrico ofrece 1.680 frecuencias UHF sintonizables en un ancho de banda de 42 MHz para una recepción libre de interferencias. Es altamente ampliable: puedes enlazar hasta 12 receptores para configuraciones simultáneas. Además, disfrutarás de un alcance de transmisión de 100 metros y hasta 8 horas de funcionamiento.

El sistema inalámbrico B1 UHF está diseñado para adaptarse a una amplia variedad de aplicaciones, incluyendo presentaciones musicales en vivo, instalaciones fijas, sistemas de megafonía, empresas de alquiler de equipos de audio y video, y lugares de culto. Ofrece todas las ventajas de un sistema inalámbrico profesional de alta calidad a un precio sumamente accesible.', 3, 'anleon/sistema_inalambrico_anleon_b1_microfono_vocal_alcance_100_metros.png', 'true', 'false', 'false', 12, 3);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (23, 'Caja Potenciada Alto Professional Ts415 Ts4 Series 2500 Watt Bluetooth', 1143964.8, 1271072.0, 15, 'Alto Pro TS415 - Altavoz alimentado de 2 vías de 15 pulgadas y 2500 vatios con Bluetooth®, DSP y control de aplicación.

2500 W pico (1600 LF + 900 HF), 1250 W RMS continuos (800 LF + 450 HF)

Características:
- Aplicación gratuita de Alto (iOS/Android) para configuración y control remoto
- Transmisión de audio Bluetooth® directa desde el dispositivo
- DSP a bordo con 4 modos de uso del altavoz (incluyendo EQ personalizado vía app)
- Conexión de altavoz estéreo inalámbrico real a través de Bluetooth®
- Mezclador integrado de 3 canales con entradas dobles combo XLR/¼", interruptores mic/línea y controles de nivel independientes
- Salida Mix XLR, controles de uso de altavoz y tamaño de subwoofer
- Driver de 15 pulgadas, bobina de voz de alta temperatura de 2.5 pulgadas (63 mm)
- Driver cerámico de salida de 1 pulgada con bobina de 1.4 pulgadas (35 mm)
- Caja ligera para transporte, montaje e instalación sencillos
- Diseño versátil: montable en poste, como monitor de suelo o suspensión con puntos M10 integrados
- Amplificadores de clase D con diseño de enfriamiento sin ventilador

Diseñado y ajustado en los Estados Unidos. Más alto. Más claro. Más inteligente.', 3, 'alto_professional/caja_potenciada_alto_professional_ts415_ts4_series_2500_watt_bluetooth.png', 'true', 'false', 'false', 13, 4);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (24, 'Consola Mixer Alto Professional TrueMix 800 FX 8 Canales', 343814.4, 382016.0, 3, 'Alto Professional TrueMix 800 FX - Mezclador compacto de 8 canales con USB, Bluetooth y Multi-FX de Alesis.

Características:
- Entrada/salida USB para reproducción de audio y grabación estéreo
- Canal Bluetooth dedicado con retorno mix-minus para emparejamiento sin retroalimentación
- Cuatro salidas de auriculares con control de volumen independiente
- 16 efectos multi-fx integrados de Alesis con canal de retorno dedicado
- Salidas principales de 1/4", Tape y AUX
- Cuatro canales de entrada de micrófono con alimentación phantom y entradas de línea balanceadas
- Dos canales de entrada estéreo con jacks TRS balanceados de 1/4"
- Ecualizador de dos bandas en todos los canales
- Entradas de 2 pistas con enrutamiento asignable: mezcla principal o salida de auriculares
- Vúmetro LED de ocho segmentos para monitoreo preciso de niveles
- Tapones de perilla adicionales incluidos para mayor personalización

El TrueMix 800 FX incluye 16 efectos como chorus, flanger y retardos y reverberaciones de alta calidad. El canal Bluetooth admite emparejamiento de teléfonos sin retroalimentación mediante tecnología mix-minus.', 3, 'alto_professional/consola_mixer_alto_professional_truemix_800_fx_8_canales.png', 'true', 'true', 'true', 11, 4);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (25, 'Caja Potenciada Alto Professional TX18S Subwoofer 900 Watt', 1071630.03, 1190700.03, 9, 'Alto Professional TX18S - Subwoofer amplificado de 18 pulgadas con DSP y 900 vatios.

Aplicaciones: Lugares medianos a grandes, estudios de ensayo, bares o discotecas, lugares de culto.

Características:
- Amplificador de potencia Clase D ultraeficiente de 900W
- Woofer de 18 pulgadas de alto rendimiento con bobina de voz de 3 pulgadas
- Ecualización y protección basada en DSP
- Modos de ecualización para música y presentaciones en vivo
- Filtro de paso bajo seleccionable (80Hz / 100Hz / 120Hz)
- Inversión de polaridad
- 2 entradas de línea combo XLR + 1/4 pulgadas
- 2 salidas de línea balanceadas XLR
- Diseño con puerto y rejilla metálica completa
- Gabinete de MDF reforzado con puerto frontal y soporte para poste de 36 mm
- Acabado resistente con pintura pulverizada texturizada
- Asas laterales para fácil transporte', 1, 'alto_professional/caja_potenciada_alto_professional_tx18s_subwoofer_900_watt.png', 'true', 'true', 'false', 13, 4);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (26, 'Caja Potenciada Alto Professional UBER FX MK2 Portatil Bateria Interna Bluetooth 200w', 740027.7, 822253.0, 13, 'Alto Professional UBER FX MK2 - Altavoz Portátil de 200W con Batería y Sonido de 320 Grados.

- Sonido de 320 Grados: sistema innovador de 200W con 5 altavoces que llena la habitación
- Batería para Todo el Día: hasta 100 horas de sonido con una sola carga
- Fácil de Transportar: asa telescópica y ruedas integradas
- Mezclador integrado de 2 canales para micrófono/línea/instrumento con ecualizador y efectos
- Transmisión con Bluetooth 5.0 y control vía app Alto Pro Control (iOS/Android)
- Enlace estéreo de altavoces vía Bluetooth
- Dos puertos USB de carga integrados
- Preajustes de ecualización para música y presentaciones en vivo
- Entrada auxiliar adicional de 3.5 mm
- Compartimento superior de almacenamiento, abrebotellas lateral y luz frontal', 4, 'alto_professional/caja_potenciada_alto_professional_uber_fx_mk2_portatil_bateria_interna_bluetooth_200w.png', 'true', 'false', 'false', 14, 4);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (27, 'Microfono Bare Knuckle Humbucker Old Guard Black Set', 273555.9, 303951.0, 5, 'Bare Knuckle Humbucker Old Guard Black Set

Aplicaciones: Tonos de blues, rock, country, pop y alternativos.
Idoneidad: Todas las guitarras de cuerpo sólido, semi-acústicas y de cuerpo hueco, o cualquier guitarra que se beneficie de un tono cálido, brillante y más dinámico.

Especificaciones:
Position: Bridge | DC Resistance: 9 kΩ | Magnet: Alnico 2 | 50 mm
Position: Neck | DC Resistance: 7.9 kΩ | Magnet: Alnico 2', 4, 'bare_knuckle/microfono_bare_knuckle_humbucker_old_guard_black_set.png', 'true', 'false', 'false', 15, 5);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (28, 'Microfono Bare Knuckle Juggernaut Black Battleworn Soapbar Set 8 Cuerdas', 639334.8, 710372.0, 12, 'Bare Knuckle Juggernaut Black Battleworn Soapbar Set 8 Cuerdas

Ya sea que se trate de tonos rítmicos aplastantes, tonos solistas fluidos o paisajes sonoros limpios y masivos, las humbuckers Juggernaut ofrecen todos los niveles. El Juggernaut es el humbucker característico del guitarrista de Periphery, Misha Mansoor, diseñado teniendo en cuenta su estilo de ejecución progresiva.

"El Bare Knuckle Juggernaut encapsula todo lo que busco en una pastilla de una manera innovadora. Finalmente puedo tener la tensión y el ataque de una cerámica con la dinámica y la naturaleza musical de un Alnico. Puedo llamar con orgullo al Bare Knuckle Juggernaut mi juego de pastillas de firma." — Misha Mansoor.

El Juggernaut está diseñado con bobinas de doble tornillo simétricamente enrolladas a mano y tiene una combinación única de flankers masivos de Alnico V y cerámica VIII para el puente, y un Alnico V de tamaño personalizado en el cuello. La respuesta de graves es grande y enfocada con mucho peso en los medios para la máxima definición a través de complejas voces de acordes extendidos. La gama alta es rica y vocal con toda la articulación y el control dinámico que Misha exige.', 4, 'bare_knuckle/microfono_bare_knuckle_juggernaut_black_battleworn_soapbar_set_8_cuerdas.png', 'true', 'true', 'false', 15, 5);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (29, 'Microfono Bare Knuckle Humbucker VHII Neck Black', 224421.3, 249357.0, 7, 'Bare Knuckle Humbucker VHII Neck Black

Agudos cristalinos, bajos definidos y la salida versátil de una humbucker vintage establecen lo último en overdrive limpio e incluso una respuesta armónica con el humbucker VHII.

Los enfoques totalmente únicos de las bobinas asimétricas permiten conservar una claridad fenomenal al tiempo que maximiza la salida del cable de esmalte liso 42 AWG. Expresado para capturar la energía cruda original y el sonido marrón de finales de los 70, el imán Alnico V de corte vintage permite una sensación realmente abierta y sensible al tacto.

Los armónicos son fuertes y definidos con una excelente separación de cuerdas, produciendo un sonido enorme con un excelente ataque de púas incluso con cantidades extremas de ganancia de preamplificador. El diseño de las bobinas permite excelentes opciones de división y paralelo, y funciona extremadamente bien con selectores de tono giratorios.', 5, 'bare_knuckle/microfono_bare_knuckle_humbucker_vhii_neck_black.png', 'true', 'false', 'false', 15, 5);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (30, 'Guitarra Electrica Chapman ML2 Buttercream Satin NewOldStock', 899100.0, 999000.0, 14, 'Guitarra Electrica Chapman ML2 Buttercream Satin

Hace diez años, Chapman Guitars lanzó la ML2, nuestra propia interpretación simplificada de un clásico. Una década después, estamos relanzando la ML2 como un modelo ajustado, refinado y redefinido.

Con nuestro enfoque en la estabilidad de afinación y la jugabilidad, hemos empleado un "ángulo de cuerda satisfactoriamente recto" a través de nuestro nuevo diseño de pala "Pennant", creando un equilibrio de tensión en las cuerdas. Todos los ingredientes correctos están en su lugar para ofrecer una variedad de tonos junto con una jugabilidad superior.

Características:

ARCE Y ÉBANO, PERFECCIÓN
Un diapasón de ébano Macassar en un mástil de arce flameado es una combinación irresistible. El tallado de mástil en forma de C, los bordes redondeados del diapasón y el acabado satinado hacen que esta guitarra sea suave de tocar.

CONSTRUCCIÓN DEL CUERPO PREMIUM
El cuerpo delgado y ligero de caoba con chapa de fresno satinado es una exquisita mezcla de forma y función, ergonómicamente contorneado con una base tonal equilibrada. Perfecto para el músico de géneros cruzados.

PASTILLAS
Equipada con un par de pastillas Chapman Stentorian Zero humbucker con amplia gama tonal. Consigue tonos contundentes y saturados con alta ganancia, o tonos limpios cristalinos a través del interruptor de 3 vías y la función de división de bobina en el potenciómetro de tono.', 1, 'chapman_guitars/guitarra_electrica_chapman_ml2_buttercream_satin_newoldstock.png', 'true', 'false', 'false', 16, 6);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (31, 'Púas Clayton Duraplex Pick Standard Pack X 12 Unidades', 7290.0, 8100.0, 5, 'Púas Clayton Duraplex Pick Standard Pack X 12 Unidades

Duraplex ha estado en el mercado de las púas de guitarra durante años. Lo que distingue a nuestra Duraplex de otras es que utilizamos la forma más resistente del material para evitar muescas y brindar una resistencia máxima. Además, nuestros bordes están pulidos, ¡así que no hay pestañas molestas que se interpongan en tu camino!', 10, 'clayton/puas_clayton_duraplex_pick_standard_pack_x12_unidades.png', 'true', 'false', 'false', 17, 7);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (32, 'Púas Clayton Hexpick Duraplex Standard Pack X 12 Unidades', 7290.0, 8100.0, 4, 'Púas Clayton Hexpick Duraplex Standard Pack X 12 Unidades

Duraplex ha estado en el mercado de las púas de guitarra durante años. Lo que distingue a nuestra Duraplex de otras es que utilizamos la forma más resistente del material para evitar muescas y brindar una resistencia máxima. Además, nuestros bordes están pulidos, ¡así que no hay pestañas molestas que se interpongan en tu camino!', 10, 'clayton/puas_clayton_hexpick_duraplex_standard_pack_x12_unidades.png', 'true', 'false', 'false', 17, 7);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (33, 'Púas Clayton Black Raven Pick Small Teardrop Pack X 12 Unidades', 7290.0, 8100.0, 0, 'Púas Clayton Black Raven Pick Small Teardrop Pack X 12 Unidades

Esta púa ha sido especialmente formulada para reducir ese molesto sonido de cuerda al golpear. Además, tiene una superficie mate que te permite agarrar la púa sin ningún deslizamiento no deseado.', 10, 'clayton/puas_clayton_black_raven_pick_small_teardrop_pack_x12_unidades.png', 'true', 'false', 'true', 17, 7);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (34, 'Pedalera Para Bajo Darkglass AGM Anagram Multifuncion Pantalla Tactil', 2178981.54, 2421090.6, 10, 'Darkglass ANAGRAM - Estación de trabajo insignia para bajistas

Presentamos ANAGRAM, la estación de trabajo insignia para bajistas de Darkglass Electronics. Diseñado para revolucionar la manera en que los bajistas abordan su arte, ANAGRAM combina 15 años de innovación con tecnología de última generación, ofreciendo un universo de posibilidades tonales en una única plataforma creada específicamente para el bajo.

Diseñado para un rendimiento superior:
ANAGRAM funciona con un procesador hexacore de vanguardia que ofrece una latencia ultra baja para una interpretación fluida y en tiempo real. En su núcleo se encuentra un procesamiento de audio impecable de 32 bits/48kHz, que garantiza claridad, fidelidad y un nivel de ruido extremadamente bajo con calidad profesional.

Integrado con Neural Amp Modeler (NAM), ANAGRAM te permite utilizar miles de modelos de amplificadores y efectos generados por usuarios. Cada detalle ha sido meticulosamente diseñado para brindar una experiencia enfocada en el bajo, permitiéndote moldear desde calidez analógica hasta paisajes sonoros innovadores.', 2, 'darkglass/pedalera_para_bajo_darkglass_agm_anagram_multifuncion_pantalla_táctil.png', 'true', 'false', 'false', 18, 8);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (35, 'Pedal Darkglass HYL Hyper Luminal Compressor Para Bajo Guitarra', 548666.1, 609629.0, 11, 'Darkglass Hyper Luminal Compressor

El Compresor Hyper Luminal cuenta con el primer diseño híbrido en un pedal compresor: un VCA análogo controlado por sidechain digital captura los caracteres de algunos de los compresores más legendarios de la historia, manteniendo la trayectoria de la señal completamente análoga.

Controles:
- BLEND: Mezcla la señal limpia y procesada. Colocado antes del control Output, permite usar el Hyper Luminal como booster transparente.
- TIME: Establece las constantes de tiempo (Ataque y Liberación). Personalizable via Darkglass Suite.
- OUTPUT: Establece el volumen de salida general.
- COMPRESSION: Establece la cantidad de compresión general y afecta la ganancia de compensación interna.
- RATIO: Ajusta la cantidad de compresión.
- MODE: Selecciona el Modo (BUS, FET, o SYM).
- USB: Conector Micro USB B para conectar a PC/Mac y configurar ajustes via Darkglass Suite.

Dimensiones: 75 x 111 x 43 mm', 4, 'darkglass/pedal_darkglass_hyl_hyper_luminal_compressor_para_bajo_guitarra.png', 'true', 'false', 'false', 19, 8);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (36, 'Amplificador Darkglass DG210A Microtubes 500 Combo 210 Para Bajo', 3094331.4, 3438146.0, 16, 'Darkglass DG210A Microtubes 500 Combo 210 - Redefiniendo el Bajo con Precisión

Diseñada para ofrecer la máxima calidad sonora y portabilidad, la Serie M Combo define la excelencia en tonos de bajo analógicos. Equipada con altavoces Eminence® hechos a medida y alimentada por un módulo de potencia clase D de 500 W.

Características del Panel Superior:
- Entrada: Conector ¼" mono estándar.
- Salida de Auriculares: Con emulación de gabinete analógico.
- Pasivo/Activo: Botón para cambiar entre modo pasivo y activo.
- Compresión: Controla la cantidad de compresión dinámica con ajuste automático de ganancia de compensación.
- Drive: Controla la distorsión del Motor Microtubes. Presionar selecciona el modo: OFF / Vintage Microtubes / Microtubes B3K.
- Mezcla: Mezcla entre señal Limpia y señal de Distorsión.
- Nivel: Controla el volumen de salida del Motor Microtubes.
- Bajos: ±12 dB @ Estantería Baja.
- Medios Bajos: ±12 dB @ 500 Hz / 1 kHz (frecuencia seleccionable).
- Medios Altos: ±12 dB @ 1.5 kHz / 3 kHz (frecuencia seleccionable).', 1, 'darkglass/amplificador_darkglass_dg210a_microtubes_500_combo_210_para_bajo.png', 'true', 'true', 'true', 20, 8);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (37, 'Potenciometros Preamp Darkglass Tone Capsule Dtc', 212025.6, 235584.0, 0, 'Darkglass Tone Capsule

La Tone Capsule es una modalidad nueva e inusual de preamplificadores incorporados. Está diseñada para respetar el carácter natural de tu instrumento mientras expande exponencialmente las posibilidades sonoras.

La Tone Capsule es única en el sentido que no tiene un control de agudos estándar. La idea fue de Sheldon Dingwall: en lugar de Bass-Mid-Treble convencional, sugirió incluir un segundo control de medios que puede configurarse para operar en el extremo más alto del espectro, ofreciendo todos los beneficios de un control de agudos (mayor claridad y definición al boostear) pero con una operación más natural, menos dura y silenciosa.', 5, 'darkglass/potenciometros_preamp_darkglass_tone_capsule_dtc.png', 'true', 'false', 'false', 21, 8);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (38, 'Cabezal Para Bajo Darkglass Microtubes 900v2', 2766695.4, 3074106.0, 17, 'Darkglass Microtubes 900 v2

Hace tres años, Darkglass Electronics lanzó su primer amplificador, el Microtubes 900. Sus características inusuales y su diseño encarnaron el espíritu de Darkglass como ninguno de sus productos anteriores: intransigente, increíblemente versátil y sin disculpas por su volumen.

El Microtubes 900 v2 presenta el siguiente paso en su evolución con mayor durabilidad, ecualizador mejorado, compresión de calidad de estudio, emulación de gabinete de respuesta de impulso y control MIDI, ofreciendo todas las opciones que el bajista profesional moderno necesita en un formato compacto, elegante y potente.', 2, 'darkglass/cabezal_para_bajo_darkglass_microtubes_900v2.png', 'true', 'false', 'false', 22, 8);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (39, 'Preamplificador Simplifier MK2 Para Guitarra Cabsim Estereo DSM Humboldt', 673251.3, 748057.0, 10, 'SIMPLIFIER MK-II
Lo último en simulación de amplificadores analógicos
El nuevo gigante de tu pedalera
 
El Simplifier Classic de DSM Humboldt Electronics ha sido un gran éxito entre los guitarristas, por lo que su emoción no fue sorprendente cuando se anunció el Simplifier mk2. Repleto de las mismas simulaciones de amplificador, etapa de potencia y cabinas, así como una serie de nuevos controles, el Simplifier mk2 ofrece el mismo tono potente a cualquier pedalera con mucha menos complicación. Tres excelentes preamplificadores incluyen características AC BRIT, American y MS Brit sin necesidad de hardware adicional. Estos sonidos en particular se combinan mejor con la etapa de potencia dedicada del mk2, que ofrece aún más ajustes con un interruptor de tipo de potencia mejorado y una perilla de control de distorsión lineal. De manera similar, la simulación de cabina estéreo del Simplifier combina selecciones de combo, twin y stack con opciones de selección de color para ofrecer voces de cabina independientes para los canales izquierdo y derecho. Lo mejor de todo es que DSM Humboldt se aseguró de incluir reverb de placa ajustable para agregar la cantidad perfecta de control de ambiente a tu configuración para una autenticidad completa. Si estás buscando adentrarte en sistemas de escenario silencioso o necesitas un amplificador ligero y compacto, echa un vistazo al Simplifier mk2.', 9, 'dsm_humboldt/preamplificador_simplifier_mk2_para_guitarra_cabsim_estéreo.png', 'true', 'false', 'false', 23, 10);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (40, 'Pedal Preamplificador DSM Humboldt Simplifier X Zero Watt Stereo', 916839.0, 1018710.0, 12, 'BIENVENIDO AL X
El simulador de amplificadores analógicos más avanzado jamás creado.
El SIMPLIFIER X fue diseñado y desarrollado minuciosamente para satisfacer las necesidades de los guitarristas que buscan versatilidad, flexibilidad, practicidad y, por supuesto, la capacidad de obtener los mejores tonos jamás producidos por equipos analógicos.
 
Daniel Schwartz
CPO & Fundador
 
SIN MENÚS COMPLEJOS.
CERO LATENCIA.
SONIDO Y SENSACIÓN ULTRA REALISTA.
LO QUE VES ES LO QUE OBTIENES.', 11, 'dsm_humboldt/pedal_pre_amplificador_dsm_humboldt_simplifier_x_zero_watt_stereo.png', 'true', 'true', 'false', 23, 10);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (41, 'Pedal Preamplificador DSM Humboldt Simplifier Bass Master Para Bajo', 673252.2, 748058.0, 9, 'DSM & HUMBOLDT SIMPLIFIER BASS MASTER
Nuestro nuevo Simplifier Bass Master es la culminación de años de investigación sobre los distintos factores que interactúan para lograr un tono de bajo superlativo, capaz de adaptarse a la más amplia gama de estilos y situaciones.
 
NUEVOS MODELOS DE AMPLIFICADOR
Un preamplificador súper versátil con 3 modos (Clean, Comp y Hot), mezcla de señal en paralelo con opciones de filtro de paso bajo para mejorar la sensación y respuesta de las frecuencias bajas, y un ecualizador de 4 bandas, que lo convierte en una herramienta extremadamente versátil y capaz, logrando tonos con los que otros preamplificadores de bajo solo podrían soñar.
 
NUEVO SIMULADOR DE GABINETE
Al final de la cadena de señal, nuestra exclusiva simulación analógica de gabinete permite al usuario seleccionar fácilmente el gabinete de sus sueños, eligiendo el Tamaño (4x10, 8x10 y 1x15), el Tipo de parlante (Warm, Bright o Modern), la respuesta de subgraves, y la mezcla de Tweeter para configurar diferentes niveles de brillo.

CARACTERÍSTICAS PRINCIPALES
El loop de efectos pre-FX puede asignarse al preamp, a la cadena paralela o a ambas al mismo tiempo, permitiendo usar efectos diferentes en cada ruta sin necesidad de splitters ni cables adicionales.
Las salidas XLR son "Main" y "Parallel", lo que permite a los usuarios enviar cada señal a diferentes dispositivos o canales, ya sea para grabaciones reamp o para conectar un subwoofer dedicado a los subgraves.
Además, incluye una salida de audífonos con entrada auxiliar, y dos salidas TS con opciones de Parallel-Thru y Bypass del simulador de gabinete en la salida Main.', 8, 'dsm_humboldt/pedal_preamplificador_simplifier_bass_master_para_bajo.png', 'true', 'false', 'false', 24, 10);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (42, 'Pedal DSM Humboldt Dumblifier Overdrive Special Para Guitarra', 1079999.1, 1199999.0, 13, '¿QUÉ NOS DISTINGUE?
Precisión analógica: A diferencia de los procesadores digitales, el Dumblifier responde de manera orgánica a la dinámica de tu interpretación, ofreciendo la inconfundible "compresión con pegada" y el sustain suave característicos de los amplificadores Dumble.
— Daniel Schwartz, CPO & Founder
 
¿POR QUÉ EL DUMBLIFICADOR?
Durante décadas, guitarristas de todo el mundo han soñado con capturar la magia del mítico Dumble Overdrive Special. Hasta ahora, la única forma de aproximarse a esta experiencia ha sido mediante el modelado digital: soluciones que, aunque reproducen el sonido, siempre se quedan cortas a la hora de replicar lo que realmente hace legendarios a estos amplificadores: la sensación al tacto. El Dumblifier Overdrive Special de DSM Humboldt Electronics rompe esa barrera. Mediante nuestra probada tecnología de modelado de amplificadores analógicos, no solo hemos recreado el sonido, sino también la compresión y la respuesta táctil únicas que hacen que cada nota florezca, se sostenga y cante, igual que en los amplificadores originales.', 13, 'dsm_humboldt/pedal_dsm_humboldt_dumblifier_overdrive_special_para_guitarra.png', 'true', 'false', 'true', 19, 10);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (43, 'Pedal DemonFx Sim Amp Bass Station Para Bajo', 138915.0, 154350.0, 11, 'Demonfx SIM-AMP Simplifier Bass Station
Simulador de Preamp, Power Amp y Cabina Estéreo con Salida DI para Bajo Eléctrico

LA PLATAFORMA DEFINITIVA PARA BAJO
El nuevo Demonfx SIM-AMP Simplifier Bass Station es todo lo que necesitas para conectarte directamente al sistema de sonido o grabar tonos de bajo increíbles sin comprometer calidad ni presencia.

Incluye:
Preamp para bajo con ganancia, nivel y ecualizador de 3 bandas con control de medios semi-paramétrico.
Ruta de señal paralela con filtro de paso bajo seleccionable.
Doble loop de efectos (para preamp y señal paralela).
Simulación de cabina analógica, basada en el aclamado Omnicabsim® de DSM Noisemaker.

PREAMPLIFICADOR VERSÁTIL
El preamp se basa en el Ampeg SVT®, conocido por su carácter, versatilidad y articulación. Su ecualizador flexible permite ajustes de ±15dB por banda y una selección de medios en 400Hz, 900Hz o 1500Hz.

Ganancia ajustable: mantiene un tono definido en la mayoría de los niveles, pero a mayores valores ofrece una saturación poderosa, con el mismo "gruñido" característico del SVT.', 7, 'demonfx/pedal_demonfx_sim_amp_bass_station_para_bajo.png', 'true', 'false', 'false', 18, 9);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (44, 'Pedal DemonFx Gravity Overdrive Para Guitarra', 121378.02, 134864.47, 8, 'Gravity es nuestra interpretación de dos circuitos de overdrive favoritos de todos los tiempos: el circuito estilo Klon Centaur y un circuito TS10, ¡todo en un solo pedal! Este nuevo overdrive doble se especializa en realzar las frecuencias medias, brindándote la capacidad de destacar en cualquier situación dentro de la mezcla.

La inspiración para este pedal se encuentra en su nombre, Gravity, y también en los tonos de plomo en vivo posteriores de John Mayer. En particular, el tono del solo de cierre en su canción "Gravity" y el inicio en su canción "Belief", donde apila estos dos pedales para obtener ese tono característico con una gruesa pared de frecuencias medias.

El TS10 se utiliza a menudo como el tono principal de plomo, y el K-overdrive se agrega como una segunda etapa de ganancia en cascada, ya sea como un pre-drive hacia el TS10 o como un post-drive.

Hemos recreado los circuitos en cada pedal manteniéndonos fieles a los originales, pero hemos agregado opciones de conmutación para dar forma adicional al tono. Hemos conservado ambos buffers que se utilizaron en los diseños originales para replicar la interacción exacta entre los dos circuitos.', 3, 'demonfx/pedal_demonfx_gravity_overdrive_para_guitarra.png', 'true', 'false', 'false', 25, 9);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (45, 'Pedal DemonFx YJM308 Overdrive Preamp Para Guitarra', 63504.0, 70560.0, 7, 'Descripción del Pedal Multi-Efectos (Boost/Distortion/Preamp/Overdrive)

Este versátil pedal combina cuatro modelos clásicos de efectos en uno solo, proporcionando a los guitarristas una paleta tonal diversa en un solo dispositivo compacto. Basado en los legendarios pedales MXR Distortion+, MXR Micro Amp, DOD 250 Overdrive y DOD YJM308, este pedal ofrece una amplia gama de posibilidades sonoras, desde impulsar tu tono hasta distorsiones potentes y preamplificadores expresivos.

Características Principales:
Boost/Distortion/Preamp/Overdrive: Conmuta entre cuatro modos distintos para adaptar tu sonido a diversas situaciones musicales. Ya sea que necesites un impulso limpio, una distorsión rica, un preamplificador expresivo o un overdrive cálido, este pedal tiene todo cubierto.

Clipping Toggle: Personaliza tu sonido aún más con el interruptor de clipping, que te permite elegir entre diferentes modelos de clipping para ajustar la respuesta de distorsión según tus preferencias.

Construcción Robusta: Diseñado para resistir las demandas del escenario y el estudio, este pedal presenta una construcción robusta y duradera que garantiza un rendimiento confiable en cualquier situación.

Fácil de Usar: Con controles intuitivos para LED (efecto encendido), footswitch (bypass de efecto), entrada y salida de 6.35 mm, así como alimentación de 9 V DC, este pedal es fácil de incorporar a tu configuración de pedalera.

True Bypass: Evita la pérdida de tono cuando el efecto está apagado, manteniendo la integridad de tu señal original.', 0, 'demonfx/pedal_demonfx_yjm308_overdrive_preamp_para_guitarra.png', 'true', 'false', 'false', 25, 9);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (46, 'Pedal DemonFx Ravine Delay Reverb Para Guitarra', 154791.0, 171990.0, 9, 'Revine
(Basado en el Keeley Caverns Delay Reverb V2)

El Revine es un pedal de efectos dual que combina delay y reverb, convirtiéndose en el cierre perfecto para cualquier pedalera. Ofrece un delay de estilo analógico con opción de modulación, inspirado en las cintas de eco. Con 650ms de cálido delay, se mezcla con reverberación tipo spring, shimmer, o reverb modulada. El Revine incluye una opción de true bypass o "trails" para permitir que las colas de la reverb se desvanezcan de forma natural. Gracias a su diseño compacto, este pedal encaja perfectamente en cualquier pedalera pequeña o fly rig con espacio limitado. Ha sido diseñado y afinado durante más de 2 años para combinar los efectos basados en el tiempo más populares de Keeley.

Características del Reverb
Modo Spring: Reverberación de estilo amplificador blackface con trémolo tipo F-Style
Modo Modulación: Añade una modulación coral al reverb para un espacio sonoro enorme y cavernoso
Modo Shimmer: Reverberación con énfasis en voces de octava alta en las colas del reverb
Este pedal ofrece una impresionante mezcla de sonidos que te permitirá crear texturas envolventes y espaciales, ideal para cualquier estilo musical que requiera un toque de profundidad y dimensión.', 2, 'demonfx/pedal_demonfx_ravine_delay_reverb_para_guitarra.png', 'true', 'true', 'false', 19, 9);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (47, 'Afinador de Clip Cromatico Para Guitarra Bajo Ukelele Violin Flamma FT01 Blanco', 39690.0, 44100.0, 6, 'Un afinador de guitarra y bajo con clip bien diseñado FT-01 es el afinador perfecto para su diario usar.
Una pantalla brillante y colorida, una interfaz de usuario intuitiva y una bisagra mecánica con un la pantalla giratoria mantiene las cosas fáciles de leer en cualquier posición.
El rango de sintonización es ajustable de 435 a 445 HZ.
Apto para guitarra y bajo.
Sintonización rápida y precisa de 435 a 445 Hz
Bisagra giratoria de 180°
Modo de ahorro de energía y apagado automático
Pantalla brillante y colorida
Energía: celda de litio de 3V (CR2032) Incluida
Dimensiones: 57 mm (largo) X 27 mm (ancho) X 8 mm (alto)
Peso: 25g', 5, 'flamma/afinador_de_clip_cromatico_para_guitarra_bajo_ukelele_violin_flamma_ft01_blanco.png', 'true', 'false', 'false', 26, 12);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (48, 'Pedal Octavador Flamma FS08 Para Guitarra Electrica', 178605.0, 198450.0, 12, 'Presentamos el Pedal FLAMMA FS08 Octave: una manera sencilla de añadir capas sonoras a tu ejecución de guitarra. Este pedal ofrece un control detallado sobre un efecto cuidadosamente elaborado, permitiendo a los músicos destacar con octavas polifónicas adicionales. Los músicos pueden añadir simultáneamente frecuencias de bajo adicionales y darle brillo a sus agudos con un rango de una o dos octavas adicionales.

Este efecto de octava polifónica proporciona controles individuales para una creatividad sin límites y brinda a los músicos todas las herramientas necesarias para crear un sonido verdaderamente único. Los parámetros se pueden mezclar a gusto del jugador ajustando simplemente el volumen de nivel para las cuatro opciones de octava, ofreciendo un control de precisión completo.

El Pedal FLAMMA FS08 Octave proporciona una señal completamente limpia, sin distorsión para su efecto, así como control de la señal seca, permitiendo un control preciso de la intensidad entre la señal húmeda y seca.

El pedal también permite a los músicos guardar sus creaciones en siete ranuras predefinidas. Con una navegación sencilla, los músicos pueden experimentar e innovar con los parámetros del Pedal FS08 Octave y acceder fácilmente a los presets guardados anteriormente. La interfaz proporciona un sencillo botón de "Guardar/Seleccionar" y un medidor de luz LED para identificar y acceder rápidamente al preset deseado.

El efecto está contenido en una resistente carcasa metálica de color verde con un sencillo dial de ajuste para cada parámetro individual. Su diseño aerodinámico y ligero lo hace fácilmente portátil, con tan solo 0,298 kg, permitiendo a los guitarristas superponer su sonido donde quiera que vayan. Y con unas dimensiones de solo 69,82 mm (D) x 121,5 mm (W) x 50,65 mm (H), se puede colocar fácilmente en una pedalera ocupada para una salida creativa combinada.', 6, 'flamma/pedal_octavador_flamma_fs08_para_guitarra_eléctrica.png', 'true', 'false', 'false', 27, 12);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (49, 'Pedal Portatil Multiefecto Flamma FX50 Para Guitarra Electrica', 59871.6, 66524.0, 9, 'Efectos de Guitarra Portátiles
Uniéndose a la popular serie FX de FLAMMA, el nuevo FX50 es una unidad de multi-efectos para guitarra flexible y fácil de usar en un formato súper portátil. Este compacto modelo ofrece un valor increíble para músicos que buscan una solución versátil pero sencilla para practicar, componer canciones e incluso grabar.
El FX50 puede alimentarse con un adaptador de corriente de 9V DC o un par de pilas AAA. Incluye módulos de Drive, Modulación, Delay/Reverb, Ganancia y Tono, junto con 40 ritmos de batería preestablecidos y un afinador. En el núcleo de la unidad, la sección Drive proporciona una amplia gama de tonos como Clean, Overdrive, Distortion, Crunch, Fuzz y Metal, adaptándose a diversos estilos musicales.
Los módulos de Modulación y Delay/Reverb están igualmente bien equipados, ofreciendo efectos como Chorus, Flanger, Phaser y Tremolo, además de Delay, Echo, Room y Hall Reverb. Estos módulos pueden desactivarse por completo para obtener un tono "seco". El FX50 incluye 16 parches preestablecidos y permite almacenar 16 parches adicionales programados por el usuario.
El módulo de batería incorporado y la entrada Auxiliar hacen del FX50 un excelente compañero de práctica. Los 40 patrones de batería abarcan desde ritmos de pop, funk y rock en 4/4, hasta estilos como trip-hop, samba y drum''n''bass, así como configuraciones de metrónomo en tiempos irregulares. Para garantizar un excelente sonido en cualquier entorno, el simulador de cabina puede activarse para uso con auriculares o grabación, o desactivarse para una conexión directa a un amplificador mediante el jack de salida principal de ¼".
Disponible en opciones de colores llamativos como naranja y verde, el FX50 incluye un práctico clip para cinturón y patas de goma para uso en escritorio.', 3, 'flamma/pedal_portátil_multiefecto_flamma_fx50_para_guitarra_eléctrica.png', 'true', 'false', 'false', 27, 12);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (50, 'Consola Digital Flamma FM10 Con Efectos Amp Sim', 275488.2, 306098.0, 11, 'Flamma FM10
Flamma Innovation continúa ampliando su linea con la consola de mezcla portátil FM10.
El FM10 ofrece toda la funcionalidad de una mesa de mezclas tradicional, pero también incluye características modernas, como conexiones USB tipo C para alimentación y transferencia de datos, así como un solo puerto USB-OTG para conectarse directamente a su dispositivo inteligente.
Con seis canales de entrada, el FM10 brinda una excelente flexibilidad para una variedad de instrumentos, micrófonos o reproductores de audio externos en estéreo o mono.
Cuatro salidas de audio, un interruptor de impedancia de instrumento, alimentación phantom de 48 V y una interfaz tradicional facilitan la configuración y la reproducción desde el primer momento.
Las características únicas del FM10 incluyen una función de bucle invertido para reproducir audio durante la grabación o transmisión en vivo y efectos de instrumentos incorporados, como un simulador de amplificador, reverberación, compresor y interruptor de ecualización.
También se incluyen controles separados de volumen principal, USB y de canal, así como conectores auxiliares de audio y salida de auriculares.', 7, 'flamma/consola_digital_flamma_fm10_con_efectos_amp_sim.png', 'true', 'false', 'false', 28, 12);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (51, 'Soporte Plegable Flanger FL04 Guitarra Bajo Ukelele Aluminio', 26004.6, 28894.0, 10, 'Diseño patentado de canal de guía y construcción de cierre de bloqueo para fijar tanto el tubo vertical como el tubo inferior.
No solo logra desmontabilidad y portabilidad, sino que también asegura la rigidez mecánica del soporte.

Características
1.Tubing: aleación de aluminio de alta resistencia
2.Kit de conexión: ABS puro
Colocación 3.Rod: acero galvanizado
4.Peso neto: alrededor de 375 g', 4, 'flanger/soporte_plegable_flanger_fl04_guitarra_bajo_ukelele_aluminio.png', 'true', 'false', 'false', 32, 11);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (52, 'Soporte Movil 5 Guitarras Flanger FL11W Desmontable Plegable', 65012.4, 72236.0, 8, 'Construcción resistente: Este soporte multi-rack está fabricado con acero robusto, proporcionando un soporte fuerte y flexible para una aplicación estable y duradera.
Protección acolchada: Los tubos de espuma acolchada protegen todos los puntos de contacto y aseguran que el acabado de tu guitarra se mantenga intacto. Adecuado para guitarras acústicas o eléctricas y bajos.
Ruedas móviles: Con ruedas para mover fácilmente el soporte de guitarra. Ideal para bandas de música, estudios de grabación, artistas en el escenario, escuelas, tiendas y más.
Ajuste de equilibrio: Si el soporte no está equilibrado después del montaje, ajusta la altura del tornillo para nivelarlo.
Goma de alta calidad: Hecho de goma de alta calidad, duradera, resistente al desgaste y excelente en resistencia al deslizamiento.', 4, 'flanger/soporte_móvil_5_guitarras_flanger_fl11w_desmontable_plegable.png', 'true', 'false', 'false', 32, 11);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (53, 'Banquito Apoya Pie Flanger FM-5014 Para Guitarra', 7557.3, 8397.0, 11, 'Ancho: 10 cm
Largo: 25.5 cm
Peso: 500 gr', 8, 'flanger/banquito_apoya_pie_flanger_fm-5014_para_guitarra.png', 'true', 'false', 'false', 33, 11);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (54, 'Atril Director Plegable Flanger FMS05 Para Partituras Libros Notebook', 31422.57, 34913.97, 7, 'Atril plegable y con aletas para soportar hojas
Fabricado en Aluminio
Peso: 760g
Altura: 75,5cm-148,5cm', 6, 'flanger/atril_director_plegable_flanger_fms05_para_partituras_libros_notebook.png', 'true', 'false', 'false', 33, 11);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (55, 'Muteadores De Cuerdas Gruvgear Fretwraps Bajos Y Guitarras', 18442.8, 20492.0, 10, '*** CONSULTAR MEDIDAS Y COLORES DISPONIBLES ***
Finalmente, un accesorio profesional para silenciar cuerdas que todo estudio, músico de sesión y aficionado al tapping debería tener. Desliza un FretWrap para cortar efectivamente los armónicos y la resonancia durante la grabación, actuaciones en vivo, tapping con ambas manos, o cualquier situación creativa donde necesitas esa mano adicional para obtener tomas más limpias sin el ruido no deseado de las cuerdas o el zumbido.

La correa ajustable te permite afinar la presión y el silenciamiento de las cuerdas. Se desliza rápidamente sobre el clavijero cuando no está en uso. ¡No se requiere modificación especial en la guitarra, instalación ni herramientas, pero es sorprendentemente efectivo!

SM - Se adapta a bajos de 4 cuerdas, guitarras eléctricas y acústicas de 6 cuerdas, y ukuleles
MD - Se adapta a bajos de 5 cuerdas, guitarras clásicas de 6 cuerdas
LG - Se adapta a bajos de 6 cuerdas y guitarras eléctricas de 7, y 8 cuerdas
XL - Se adapta a bajos de 7 a 12 cuerdas, Chapman Sticks, contrabajos y otras guitarras de rango extendido', 3, 'gruvgear/muteadores_de_cuerdas_gruvgear_fretwraps_bajos_y_guitarras.png', 'true', 'false', 'false', 33, 13);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (56, 'Pedalera Sheeran Looper+ 4 Modos Single Multi Sync Song', 783877.5, 870975.0, 10, 'Sheeran Looper +
Pedal de Looping de Doble Pista
Diseñado por Ed Sheeran y su equipo de producción
Flujo de trabajo intuitivo de Sheeran Looper™ de una y dos pistas
Con 4 modos de looper: Single, Multi, Sync y Song
Pedales de aluminio fundido increíblemente duraderos, como los utilizados en el looper del escenario del estadio de Ed Sheeran
DSP personalizado alimentado por HeadRush® con audio profesional de 32 bits
Pantalla a color de 1.8", anillo indicador de estado de bucle LED RGB y monitoreo LED de entrada/salida
Guarde hasta 128 bucles con más de 3 horas de audio en almacenamiento interno; importe/exporte bucles a través de USB
Funciones de rendimiento de deshacer/rehacer, solo, desvanecer, invertir, 1/2 velocidad, solo y silenciar.', 8, 'headrush/pedalera_sheeran_looper+_4_modos_de_looper_single_multi_sync_y_song.png', 'true', 'false', 'false', 34, 14);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (57, 'Parlante Potenciado Headrush FRFR112 MKII 12 Pulgadas 2500 Watts Bluetooth', 1002271.5, 1113635.0, 9, 'HeadRush FRFR-112® MKII
El potente gabinete de respuesta plana de rango completo para guitarristas y bajistas – Con Bluetooth

Presentamos el FRFR-112® MKII
HeadRush FRFR-112 MKII es un potente gabinete de guitarra de respuesta plana y rango completo de 2500 vatios con Bluetooth®, altavoz de 12", controlador de compresión HF, dos entradas combo XLR + 1/4" y salida XLR.

Características del FRFR-112® MKII
Sonido Potente y Profesional - 2500 vatios de potencia máxima ( 1200 Watts Rms Reales Aproximadamente) aseguran que tengas suficiente margen para casi cualquier actuación en vivo o ensayo.
Afinado con Precisión para Modeladores de Amplificadores - El diseño del gabinete, el woofer de 12" y el controlador de compresión HF están especialmente ajustados para una entrega precisa y lineal de emulaciones de amplificadores y gabinetes.
Habilitado con Bluetooth® - Transmite música de forma inalámbrica desde tu dispositivo móvil al canal dedicado de Bluetooth® del FRFR-112 MKII.
Toda la Conectividad que Necesitas - Dos entradas combo XLR + 1/4" con controles de volumen independientes y una salida directa XLR permiten encadenar altavoces o enviar la señal a una mezcla de sonido frontal.
Se Adapta Rápidamente a Lugares y Habitaciones - El FRFR-112 MKII tiene un interruptor de elevación de tierra para eliminar problemas de ruido causados por bucles de tierra y un interruptor de ecualización HPF para ayudar a cortar mezclas de escenario confusas.
Ligero, Flexible y Robusto - Con un peso de solo 34.7 libras / 15.7 kg, el FRFR-112 MKII es resistente pero fácil de transportar y puede ser usado en posición de cuña, vertical o montado en poste.', 12, 'headrush/parlante_potenciado_headrush_frfr112_mkii_12_pulgadas_2500_watts_bluetooth.png', 'true', 'false', 'false', 35, 14);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (58, 'Pedalera Headrush Prime Amp Cloning Autotune', 2233753.2, 2481948.0, 11, 'HeadRush Prime
El modelador de efectos/amplificador/procesador vocal de guitarra más potente.
Con un procesador multinúcleo avanzado con una enorme biblioteca de efectos de guitarra integrados, emulaciones de amplificador, cabina y micrófono, clonación inteligente de amplificador/pedal y carga IR, el mejor looper de su clase y un conjunto completo de efectos vocales (que incluye el Antares Auto-Tune estándar de la industria), el HeadRush® Prime es el procesador de efectos de piso más potente, versátil y con un sonido realista jamás creado. La pantalla de alta resolución y ultra sensible de 7 pulgadas le permite tocar, deslizar y arrastrar y soltar para crear y editar instantáneamente sus equipos de una manera fácil de usar sin precedentes.', 15, 'headrush/pedalera_headrush_prime_amp_cloning_autotune.png', 'true', 'false', 'true', 19, 14);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (59, 'Guitarra Electrica Spira S407 MBK Black Satin 7 Cuerdas', 770144.4, 855716.0, 10, 'La S-407 es una potente y elegante guitarra de 7 cuerdas con un diseño sutil pero sofisticado. Diseñada para músicos que buscan tonos profundos y ricos con capacidades de rango extendido. Con un cuerpo de álamo tostado y un mástil de arce canadiense tostado, el S-407 ofrece una tocabilidad excepcional y un registro grave potente y definido. Su diapasón de Ebony Tech, con 24 trastes jumbo, garantiza una experiencia de ejecución suave y precisa, ideal para técnicas avanzadas y complejas.

Equipada con un par de pastillas humbucker Villain™ de Spira para 7 cuerdas, el S-407 genera tonos ricos y potentes. Su diseño aerodinámico y su hardware de alta calidad, junto con las clavijas de bloqueo, brindan una estabilidad de afinación excepcional y una entonación precisa, convirtiéndola en un instrumento ideal tanto para presentaciones en vivo como para sesiones de grabación.', 11, 'spira_guitars/guitarra_electrica_spira_s407_mbk_black_satin_7_cuerdas.png', 'true', 'true', 'false', 16, 15);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (60, 'Guitarra Electrica Spira S450 TPP Trans Purple Gloss', 801579.6, 890644.0, 10, 'Una poderosa arma para el rock, la S-450 está meticulosamente diseñada para músicos que exigen un tono excepcional y un atractivo visual espectacular. La S-450 cuenta con un cuerpo de álamo tostado combinado con impresionantes tapas de arce brillante o álamo spalted. Su mástil de arce canadiense tostado, con forma moderna D, y su diapasón de arce tostado a juego ofrecen una experiencia de ejecución suave y rápida, perfecta para solos intrincados y riffs pesados.

La S-450 está equipada con un set de pastillas humbucker Villain™ de Spira, hechas a medida, que producen tonos potentes y articulados, ideales para los géneros de rock y metal. El puente fijo y las clavijas de bloqueo negras aseguran una estabilidad de afinación y precisión sobresalientes.

Con 24 trastes jumbo en un diapasón con radio de 14" y una escala de 25,5", la S-450 ofrece una ejecución sin esfuerzo. El alma de doble acción y la cejuela de hueso añaden robustez a la construcción y capacidades de rendimiento de la guitarra.', 12, 'spira_guitars/guitarra_electrica_spira_s450_tpp_trans_purple_gloss.png', 'true', 'false', 'false', 16, 15);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (61, 'Guitarra Electrica Spira T400 MWH White Satin Telecaster', 686319.3, 762577.0, 10, 'Una reinterpretación contemporánea de la clásica guitarra estilo T, la Spira T-400 combina un diseño icónico con el enfoque innovador de Spira, dando como resultado una guitarra visualmente impactante y sonoramente poderosa.

La T-400 cuenta con un cuerpo de álamo tostado y un mástil de arce canadiense tostado, lo que garantiza una durabilidad excepcional y propiedades tonales mejoradas. Su diapasón de Ebony Tech, con 24 trastes jumbo, ofrece una experiencia de ejecución suave y receptiva, ideal para una variedad de técnicas avanzadas.

Un par de pastillas humbucker Villain™ de Spira proporciona tonos autoritarios y versátiles, que destacan en configuraciones de alta ganancia. El diseño elegante de la guitarra y su hardware de primera calidad, junto con clavijas de bloqueo, aseguran una estabilidad de afinación excepcional y una entonación precisa, convirtiéndola en una compañera confiable tanto para el escenario como para el estudio.', 2, 'spira_guitars/guitarra_electrica_spira_t400_mwh_white_satin_telecaster.png', 'true', 'true', 'true', 16, 15);
INSERT INTO products (id_key, name, price, price_list, discount_percent, description, stock, image_path, is_active, is_new, is_featured, category_id, brand_id) VALUES (62, 'Funda Spira Guitars SG30 BK Para Guitarra Electrica', 94303.8, 104782.0, 10, 'La funda Spira SG30 BK ofrece una protección confiable y liviana para tu guitarra, ideal para músicos en movimiento. Diseñada para adaptarse a guitarras eléctricas estándar, esta funda combina durabilidad y practicidad con un enfoque accesible y sin complicaciones. Ya sea que te dirijas a un concierto, a un ensayo o simplemente quieras guardar tu instrumento de forma segura, la SG30 BK es una opción excelente.', 8, 'spira_guitars/funda_spira_guitars_sg30_bk_para_guitarra_electrica.png', 'true', 'false', 'false', 33, 15);

SET session_replication_role = DEFAULT;
