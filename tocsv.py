import csv
import json


# json format:
# [
#     {
#         "karuk": "ipasnáhvaanich káan úkrii.kúkuum imáan tu'ákunvar.kári xás púufich tóo ykar.xás sáruk tóo thyúrufak ástiip.xás muvêeshurak tupikniivtákishnihach.xás papúufich tóo kpúuhvarak.xás tóo thyúruripaa.xás tóo sfir.kári xás káan áraar tóo kmárihivrik.áraar pamu'áav ápap u'ávas-hunihva.xás ápap upírishhunihva.kári xás papúufich tu'êetheep.xás pa'únuhich kich tupáthih.xás tóo pvâaram.xás tóo mnish pa'únuhich.xás tu'áv.kúkuum imáan tupákunvar.",
#         "english": "Pygmy Owl lived there. Again in the morning [the next day] he went hunting. Then he killed a deer. Then he dragged it downhill to the riverbank. Then he just sat back down on top of its horns. Then he swam the deer downriver. Then he dragged it ashore. Then he skinned it. Then he met a man coming there. One side of the man's face was a spring (flowing) down. One side was plants (hanging) down. Then he (the man) took the deer away from him. Then he threw only the kidney to him.  Then he (Pygmy Owl) went home.  Then he cooked the kidney. Then he ate it. The next day, he went hunting again. [The same episode is repeated several times.]"
#     },
#     {
#         "karuk": "kári xás káan u'úum.\"ee,  ishávaas,  ôok tá ni'áhoo.nuykáreesh pa'îin púufich i'êethiipvutihat.\"kári xás pihnêefich akôor úkyav imshaxvuh'ákoor.kári xás \" chími i'ákunvar.\"kári xás uykár papúufich.xás ukpúuhvarak kúkuum.kári xás uthyúruripaa.xás kuníshfir.xás pihnêefich u'áamva paathkúrit.kári xás kúkuum pa'áraar káan u'úum.xás kúkuum papúufich kinpáthih pa'únuhich.xás upíip, \" kaneeyfúutsip.\"kári xás pihnêefich axvâak u'áaka pa'akôora mûuk.xás kuníykar.xás pihnêefich upíip, \" púya pay uum váah.\"xás kunimníshkirihva.kupánakanakana.ipasnáhvaanich ukúphaanik.",
#         "english": "Then he (Coyote) arrived there. \"Ee, nephew, I have come. We will kill the one who has been taking the deer from you.\" Then Coyote made an axe, a (pine) gum axe. Then (Coyote said), \"Go hunting!\" Then he (Pygmy Owl) killed a deer. Then he swam it down from upriver again. Then he pulled it toward land. Then they skinned it. Then Coyote ate the fat. Then the man came there again. Then again he threw the deer's kidney to them. Then he said, \"Load me up!\" Then Coyote struck him on the head with the axe. Then they killed him. Then Coyote said, \"So this is all right!\" Then they cooked it. Kupánakanakana. Pygmy Owl did it."
#     },
#     {
#         "karuk": "hã'ii!",
#         "english": "[expression]"
#     },

def cleanup(s):
    s = s.replace("\n", " ")
    # tabs too
    s = s.replace("\t", " ")
    # collapse multiple spaces into one
    s = " ".join(s.split())
    return s

def main():
    pass
    with open("karuk-translator-ui/src/translations.json", encoding="utf-8") as f:
        data = json.load(f)
    with open("training/dataset.csv", "w", encoding="utf-8", newline="") as f:
        # format into csv with header: input, instruction, output
        writer = csv.writer(f)
        writer.writerow(["input", "instruction", "output"])
        # for each json item, write 2 rows.
        # 1 row: "translate from karuk to english", karuk, english
        # 2 row: "translate from english to karuk", english, karuk
        for item in data:
            karuk = cleanup(item["karuk"])
            english = cleanup(item["english"])
            writer.writerow([karuk, "translate from karuk to english", english])
            writer.writerow([english, "translate from english to karuk", karuk])

if __name__ == "__main__":
    main()
