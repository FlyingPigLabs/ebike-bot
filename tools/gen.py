from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.enums import TA_LEFT

NAVY = Color(0.121569, 0.227451, 0.372549)
SHADE = Color(0.933333, 0.94902, 0.968627)
GRID = Color(0.772549, 0.807843, 0.85098)
GRAY = Color(0.501961, 0.501961, 0.501961)
W, H = letter
M = 32.4
CW = W - 2 * M
C1 = 104.4
ACCESSED = "11/27/2026"
TITLE = "Arizona Vehicle Type Definitions \u2014 A.R.S. \u00a728-101"

body = ParagraphStyle("b", fontName="Helvetica", fontSize=8.3, leading=9.7, alignment=TA_LEFT)
label = ParagraphStyle("l", parent=body, fontName="Helvetica-Bold")
sect = ParagraphStyle("s", fontName="Helvetica-Bold", fontSize=9.1, leading=11, textColor=white)
note = ParagraphStyle("n", parent=body, leftIndent=12, bulletIndent=4, bulletFontName="Helvetica", bulletFontSize=10, spaceAfter=2)

def P(name, cite):
    return Paragraph(f'{name} <font name="Helvetica" color="#1F3A5F">{cite}</font>', label)

def section(title, rows):
    data = [[Paragraph(title, sect), ""]] + [[P(n, c), Paragraph(t, body)] for n, c, t in rows]
    t = Table(data, colWidths=[C1, CW - C1], repeatRows=1, splitByRow=1)
    t.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BOX", (0, 0), (-1, 0), 0.25, NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, SHADE]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.5),
        ("TOPPADDING", (0, 0), (-1, -1), 1.0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
        ("TOPPADDING", (0, 0), (-1, 0), 1.8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2.2),
    ]))
    return t

S = []
S.append(section("UMBRELLA TERMS", [
 ("Vehicle", "\u00b690", "A device in, on or by which a person or property is or may be transported or drawn on a public highway. <b>Does not include:</b> electric bicycles, electric miniature scooters, electric standup scooters and devices moved by human power; devices used exclusively on stationary rails or tracks; personal delivery devices; scrap vehicles; personal mobile cargo carrying devices."),
 ("Motor vehicle", "\u00b653", "(a) A self-propelled vehicle; or, for motor vehicle fuel tax laws, a vehicle operated on the highways of this state propelled by motor vehicle fuel. (b) <b>Does not include:</b> scrap vehicle, personal delivery device, personal mobile cargo carrying device, motorized wheelchair, electric personal assistive mobility device, electric bicycle, electric miniature scooter, electric standup scooter or motorized skateboard."),
]))
S.append(Spacer(1, 5))
S.append(section("MOTORCYCLES AND MOPEDS", [
 ("Motorcycle", "\u00b650", "Motor vehicle with a seat or saddle for the rider, designed to travel on <b>not more than three wheels</b> in contact with the ground. Excludes a tractor, electric bicycle, electric miniature scooter, electric standup scooter and moped."),
 ("Motor driven cycle", "\u00b651", "A motorcycle, including every motor scooter, with a motor that produces <b>not more than 5 horsepower</b>. Excludes electric bicycles, electric miniature scooters and electric standup scooters."),
 ("Autocycle", "\u00b66", "Three-wheeled motorcycle; driver and passengers ride in a fully or partially enclosed seating area with a <b>roll cage</b>, safety belts for each occupant and antilock brakes; designed to be controlled with a <b>steering wheel and pedals</b>."),
 ("Moped", "\u00b649", "A bicycle (not an electric bicycle, electric miniature scooter or electric standup scooter) equipped with a helper motor: max piston displacement <b>50 cc or less</b>, brake horsepower <b>1.5 or less</b>, and max speed <b>25 mph or less</b> on a flat surface with less than 1% grade."),
]))
S.append(Spacer(1, 5))
S.append(section("BICYCLES AND PERSONAL DEVICES", [
 ("Bicycle", "\u00b611", "Device propelled by human power on which a person may ride (incl. a racing wheelchair) with either (a) two tandem wheels, either <b>more than 16 in.</b> in diameter, or (b) three wheels in contact with the ground, any <b>more than 16 in.</b> in diameter."),
 ("Electric bicycle", "\u00b629", "Bicycle or tricycle with <b>fully operable pedals</b> and an electric motor of <b>less than 750 watts</b>, meeting one class: <b>Class 1</b> \u2013 assists only while pedaling; stops assisting at <b>20 mph</b>. <b>Class 2</b> \u2013 motor may propel exclusively (no pedaling); cannot assist at <b>20 mph</b>. <b>Class 3</b> \u2013 assists only while pedaling; stops assisting at <b>28 mph</b>."),
 ("Electric miniature scooter", "\u00b630", "Weighs <b>less than 30 lb</b>; 2 or 3 wheels; handlebars; floorboard to stand on while riding; electric motor and/or human power; max speed <b>not over 10 mph</b>, with or without human propulsion, on a paved level surface."),
 ("Electric standup scooter", "\u00b632", "Weighs <b>less than 75 lb</b>; 2 or 3 wheels; handlebars; floorboard to stand on while riding; electric motor and/or human power; max speed <b>not over 20 mph</b>, with or without human propulsion, on a paved level surface. Does not include an electric miniature scooter."),
 ("Electric personal assistive mobility device", "\u00b631", "<b>Self-balancing</b> device with one wheel or two nontandem wheels; electric propulsion limiting max speed to <b>15 mph or less</b>; designed to transport only one person."),
 ("Motorized skateboard", "\u00b653(b)(i)", "Self-propelled device with <b>no handlebars</b>, a motor, a deck to ride on and at least two tandem wheels in contact with the ground. <i>Defined only within the \u00b653(b) exclusion.</i>"),
 ("Motorized wheelchair", "\u00b653(b)(ii)", "Self-propelled wheelchair used by a person for mobility (also \u00b663, \u00a728-601(11)). <i>Per \u00b663, a person using an EPAMD or a manual or motorized wheelchair is a pedestrian (unless the manual wheelchair qualifies as a bicycle).</i>"),
 ("Personal delivery device", "\u00b664", "Device manufactured to transport cargo and goods in an area described in \u00a728-1225, with automated driving technology operated with remote human support and supervision. Not a personal mobile cargo carrying device."),
 ("Personal mobile cargo carrying device", "\u00b665", "Electronically powered; used primarily on sidewalks and in crosswalks to transport property; <b>under 80 lb</b> excl. cargo; max <b>12 mph</b>; owner-monitored, designed to stay within <b>25 ft</b> of the owner; braking system for a controlled stop."),
]))
S.append(Spacer(1, 5))
S.append(section("LOW-SPEED AND OFF-ROAD", [
 ("Golf cart", "\u00b638", "Motor vehicle with <b>at least 3 wheels</b> on the ground; unladen weight <b>under 1,800 lb</b>; designed to be and operated at <b>not more than 25 mph</b>; designed to carry <b>not more than 4 persons</b> incl. driver."),
 ("Neighborhood electric vehicle", "\u00b656", "Self-propelled, electrically powered, emission-free motor vehicle with <b>at least 4 wheels</b>; complies with federal low-speed vehicle standards (49 CFR 571.3(b), 571.500) unless excepted/exempted under federal law."),
 ("Neighborhood occupantless electric vehicle", "\u00b657", "A neighborhood electric vehicle not designed, intended or marketed for human occupancy."),
 ("Neighborhood electric shuttle", "\u00b655", "Emission-free electric motor vehicle, at least 4 wheels, carries <b>at least 8</b> incl. driver; commercial motor vehicle (\u00a728-5201); vehicle for hire (\u00a728-9501) under \u00a728-9503 permit; meets low-speed vehicle standards. Includes non-manufacturer aftermarket modification to carry up to 15."),
 ("Motorized quadricycle", "\u00b652", "Emission-free electric motor (passenger pedals optional); at least 4 wheels; seats <b>at least 8</b> incl. driver; operable on flat ground on motor alone; commercial motor vehicle; limousine under \u00a728-9503 permit; licensed (ch. 10) manufacturer; meets low-speed vehicle standards."),
 ("All-terrain vehicle", "\u00b63", "<b>(a)</b> Motor vehicle designed primarily for recreational nonhighway all-terrain travel; <b>50 in. or less</b> wide; unladen <b>1,200 lb or less</b>; 3+ nonhighway tires; operated on a public highway. <b>(b)</b> Recreational off-highway vehicle, same design purpose; <b>80 in. or less</b> wide; unladen <b>2,500 lb or less</b>; 4+ nonhighway tires; steering wheel; rollover protective structure; occupant retention system."),
 ("Off-road recreational motor vehicle", "\u00b659", "Motor vehicle designed primarily for recreational nonhighway all-terrain travel and <b>not operated on a public highway</b>. Not a vehicle used for construction, building trade, mining or agricultural purposes."),
]))
S.append(Spacer(1, 5))
S.append(section("PASSENGER, FOR-HIRE AND EMERGENCY", [
 ("Bus", "\u00b613", "Motor vehicle designed to carry <b>16 or more</b> passengers, incl. driver."),
 ("School bus", "\u00b672", "Motor vehicle designed to carry <b>more than 10</b> passengers and either (a) owned by a public/governmental agency or other institution, or (b) privately owned and operated for compensation, to transport children to or from home or school on a regularly scheduled basis."),
 ("Limousine", "\u00b644", "Motor vehicle providing prearranged ground transportation, or operating on a regular route or between specified points, incl. under contract at a fixed rate or time; seating <b>not over 15</b> incl. driver."),
 ("Livery vehicle", "\u00b645", "Seating <b>not over 15</b> incl. driver; flat-rate or flat-hourly fare between zones or within an area; exclusive or shared-ride hire; may run a regular route or offer prearranged (\u00a728-141) or contracted on-demand service."),
 ("Taxi", "\u00b681", "Seating <b>not over 15</b> incl. driver; does not primarily operate on a regular route or between specified places; fare based on distance traveled, or prearranged service (\u00a728-141) at a predetermined fare."),
 ("Authorized emergency vehicle", "\u00b65", "(a) Fire department vehicle; (b) police vehicle; (c) ambulance or emergency vehicle of a municipal department or public service corporation designated/authorized by ADOT or a local authority; (d) other ambulance, fire truck or rescue vehicle authorized by ADOT in its sole discretion that meets its liability insurance requirements."),
]))
S.append(Spacer(1, 5))
S.append(section("TRUCKS, TRAILERS AND COMBINATIONS", [
 ("Truck", "\u00b688", "Motor vehicle designed or used primarily to carry property other than the effects of the driver or passengers; includes one with an added box, platform or other carrying equipment."),
 ("Truck tractor", "\u00b689", "Motor vehicle designed and used primarily to <b>draw other vehicles</b>; not built to carry a load other than part of the weight of the vehicle and load drawn."),
 ("Vehicle transporter", "\u00b691", "Truck tractor capable of carrying a load and drawing a semitrailer, incl. one with a stinger-steered fifth wheel or a dolly-mounted fifth wheel fastened at 2+ points."),
 ("Semitrailer", "\u00b675", "Vehicle (with or without motive power; not a pole trailer or single-axle tow dolly) designed to carry persons or property and be drawn by a motor vehicle, with <b>some part of its weight</b> and load resting on another vehicle."),
 ("Trailer", "\u00b684", "Same as above, but constructed so <b>no part of its weight</b> rests on the towing vehicle. A semitrailer with an auxiliary front axle (dolly) is deemed a trailer."),
 ("Pole trailer", "\u00a728-601(16)", "Vehicle without motive power, drawn by another vehicle and attached by a reach or pole or boomed/secured to it, ordinarily used for long or irregular loads (poles, pipes, structural members)."),
 ("Single-axle tow dolly", "\u00b676", "<b>Nonvehicle</b> device drawn by a motor vehicle, used exclusively to transport another motor vehicle with its front or rear wheels mounted on the dolly and other wheels on the ground."),
 ("Combination of vehicles", "\u00b617", "A truck or truck tractor and semitrailer and any trailer it tows; not a forklift designed to load/unload the truck, trailer or semitrailer."),
]))
S.append(Spacer(1, 5))
S.append(section("FARM, SPECIAL AND AUTOMATED", [
 ("Farm tractor", "\u00b635", "Motor vehicle designed and used primarily as a farm implement for drawing implements of husbandry."),
 ("Implement of husbandry", "\u00b643", "Vehicle designed primarily for agriculture and used exclusively in agricultural operations (manual, self-propelled, autonomous or with an automated driving system), used solely for agricultural purposes and only <b>incidentally</b> moved on a highway (between parts of a farm, between farms, or to repair, supply or storage)."),
 ("Power sweeper", "\u00b666", "Implement, with or without motive power, only incidentally operated on a street or highway, designed to remove debris from paved surfaces, and a vehicle on which it is permanently mounted."),
 ("Autonomous vehicle", "\u00b69", "Motor vehicle equipped with an automated driving system."),
 ("Fully autonomous vehicle", "\u00b637", "Autonomous vehicle with an automated driving system designed to function as <b>SAE J3016 level 4 or 5</b>; may operate solely by that system or by a human driver when it is not engaged."),
]))
S.append(Spacer(1, 5))
notes_hdr = Table([[Paragraph("READING NOTES", sect)]], colWidths=[CW])
notes_hdr.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("LEFTPADDING", (0, 0), (-1, -1), 2.5),
    ("TOPPADDING", (0, 0), (-1, -1), 1.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2)]))
S.append(notes_hdr)
S.append(Spacer(1, 4))
for n in [
 "Electric bicycles, electric miniature scooters and electric standup scooters are excluded from both \u201cvehicle\u201d (\u00b690) and \u201cmotor vehicle\u201d (\u00b653), and the moped, motorcycle and motor driven cycle definitions each expressly exclude them.",
 "\u201cMotor driven cycle\u201d (\u00b651) and \u201cautocycle\u201d (\u00b66) are each defined as a type of \u201cmotorcycle\u201d (\u00b650).",
 "A device must meet every element of a definition to fall within it. For example, a bicycle without fully operable pedals, or with a motor of 750 watts or more, is not an \u201celectric bicycle\u201d under \u00b629.",
 "Chapter 3 (traffic and vehicle regulation) has its own definitions in \u00a728-601, incl. pole trailer (16), motorized wheelchair (11) and a separate \u201ctruck\u201d (30). \u201cMotorized skateboard\u201d is defined only in the \u00b653(b) exclusion. Scrap vehicle: \u00a744-1641. Commercial motor vehicle: \u00a728-5201.",
]:
    S.append(Paragraph(n, note, bulletText="\u2022"))

def on_page(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 14)
    c.drawString(M, H - 44.4, TITLE)
    c.setFillColor(black); c.setFont("Helvetica", 7.8)
    c.drawString(M, H - 57.4, f"Text from A.R.S. \u00a728-101 (and \u00a728-601 where noted), azleg.gov, accessed {ACCESSED}.")
    c.setFont("Helvetica-Bold", 7.8); c.drawString(M, H - 67.4, "\u00b6")
    c.setFont("Helvetica", 7.8)
    c.drawString(M + 5, H - 67.4, " = paragraph of \u00a728-101. Paragraph numbers change when the section is amended \u2014 verify before citing.")
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, H - 71, W - M, H - 71)
    c.setFillColor(GRAY); c.setFont("Helvetica", 7.5)
    c.drawString(M, 32, "Reference aid only; not legal advice.")
    c.drawRightString(W - M, 32, f"Page {doc.page} of 2")
    c.restoreState()

# The file index.html already links, next to index.html. Path is relative to this script so a rebuild works from any checkout.
OUT = Path(__file__).resolve().parent.parent / "quick-reference-other-vehicles.pdf"
doc = BaseDocTemplate(str(OUT), pagesize=letter,
    title="Arizona Vehicle Type Definitions - ARS 28-101", leftMargin=M, rightMargin=M, topMargin=77, bottomMargin=40)
frame = Frame(M, 40, CW, H - 77 - 40, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
doc.build(S)
