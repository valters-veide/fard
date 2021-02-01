import fontforge
import psMat
from math import radians
import time

# Import font
sample_font = fontforge.open("/Users/valtersveide/Desktop/Gilroy-ExtraBold.ttf")

# Create new font
new_font = fontforge.font()

# Set encoding to Unicode BMP
new_font.encoding = "ISO10646-1"

new_font.fontname = "newFont#10"
new_font.familyname = "newFont#10"
new_font.fullname = "newFont#10"
#new_font.descent = 10
#new_font.ascent = 20

# Transfer default letters
sample_font.selection.select(("ranges", None), 0, 191)
sample_font.copy()

new_font.selection.select(("ranges", None), 0, 191)
new_font.paste()


# Transfer letter
def transferletter(letter, where):
    sample_font.selection.none()
    sample_font.selection.select(letter)
    sample_font.copy()

    new_font.selection.none()
    new_font.selection.select(*where)
    new_font.paste()

# Transfer glyph
class TransferGlyph:
    def __init__(self, glyph):
        self.ensure_og_state(glyph)
        self.glyph = glyph

    def change_size(self, glyph, xsize, ysize, xskew, yskew):
        move = 0
        new_font.selection.none()

        new_font.selection.select(glyph)
        new_font.transform([xsize, yskew, xskew, ysize, move, move])
        new_font.selection.none()






    def find_middle_x(self, base_layer, paste_layer, xxmove):
        xmax = base_layer.boundingBox()
        glyph_size = paste_layer.boundingBox()
        xmove = (((xmax[2] - xmax[0]) / 2) + xmax[0]) - (((glyph_size[2] - glyph_size[0]) / 2) + glyph_size[0])
        return xmove * xxmove

    def find_middle_x_at_top_y(self, base_layer, paste_layer, xxmove):
        topmiddle = self.topy_middle_x(base_layer)
        glyphmiddle = self.middle_x(paste_layer)

        xmove = topmiddle - glyphmiddle
        return xmove * xxmove

    def find_middle_glyph_bottom_x_at_top_y(self, base_layer, paste_layer, xxmove):
        topmiddle = self.topy_middle_x(base_layer)
        bottommiddle = self.bottomy_middle_x(paste_layer)

        xmove = topmiddle - bottommiddle
        return xmove * xxmove

    def find_middle_glyph_bottom_x_at_middle_y(self, base_layer, paste_layer, xxmove):
        topmiddle = self.middle_x(base_layer)
        bottommiddle = self.bottomy_middle_x(paste_layer)

        xmove = topmiddle - bottommiddle
        return xmove * xxmove

    def find_left_x_at_bottom_y(self, base_layer, paste_layer, xxmove):
        xmax = base_layer.boundingBox()

        paste_middle = self.topy_middle_x(paste_layer)
        base_left = xmax[0]
        xmove = base_left - paste_middle
        return xmove * xxmove


############ ------------------------------------ #############
############ ------------------------------------ #############
############ ~2000 koda rindiņas ---------------- #############
############ noņemtas, koncepta prezentācijas --- #############
############ nolūkos, lai saglabātu specifiku no  #############
############ autora intelektuālā īpašuma privātu. #############
############ ------------------------------------ #############
############ ------------------------------------ #############

upsideE = TransferGlyph(101)

upsideE.rotateGlyph(180, 101)
upsideE.centerMiddle(1, 1, 0, 0, 1, 1, 477)
upsideE.transferHard(477)
##############################################

where_macron_late = [481, 560, 561, 556, 557]
for character in where_macron_late:
    plusMacron.centerTop(1, 0.8, 0, 0, 0.40, 1, 1, character)
    plusMacron.transfer()

where_macron_late_spec = [480]
for character in where_macron_late_spec:
    plusMacron.topCenterChar(1, 0.8, 0, 0, 0.40, 1, 1, character)
    plusMacron.transfer()

where_acute_late = [471, 472, 510, 511]
for character in where_acute_late:
    plusAcute.centerTop(1, 1, 0, 0, acutecoef, 1, 1, character)
    plusAcute.transfer()

where_acute_late_spec = [506, 507]
for character in where_acute_late_spec:
    plusAcute.topCenter(1, 1, 0, 0, acutecoef, 1, 1, character)
    plusAcute.transfer()

where_grave_late = [475, 476]
for character in where_grave_late:
    plusGrave.centerTop(1, 1, 0, 0, gravecoef, 1, 1, character)
    plusGrave.transfer()


# Save
sec = time.localtime()
stamp = time.strftime("%d-%b | %H:%M:%S", sec)
new_font.fontname = "SpaceTest"
new_font.save("/Users/valtersveide/Test " + str(stamp) + ".otf")
print(stamp)