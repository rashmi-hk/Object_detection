from ultralytics import YOLO
import cv2
import cvzone
import math
import csv

def intersect(bbox1, bbox2):
    x1, y1, x2, y2 = bbox1
    x3, y3, x4, y4 = bbox2
    if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
        return False
    return True

def detect_objects(classNames):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    model = YOLO("best.pt")

    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        objects = []

        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get class and confidence
                cls = int(box.cls[0]) if len(box.cls) > 0 else -1
                conf = math.ceil((box.conf[0] * 100)) / 100

                # Filter out objects not in classNames
                if 0 <= cls < len(classNames) and classNames[cls] in classNames:
                    # this is for opencv bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    obj = {"class": classNames[cls], "bbox": (x1, y1, x2, y2), "confidence": conf}
                    objects.append(obj)

        # Perform intersection check to filter out overlapping objects
        filtered_objects = []
        for i, obj in enumerate(objects):
            bbox = obj["bbox"]
            is_overlapping = False
            for j, other_obj in enumerate(objects):
                if i != j:
                    other_bbox = other_obj["bbox"]
                    if intersect(bbox, other_bbox):
                        is_overlapping = True
                        break
            if not is_overlapping:
                filtered_objects.append(obj)

        # Draw bounding boxes and text for filtered objects
        for obj in filtered_objects:
            x1, y1, x2, y2 = obj["bbox"]
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            cvzone.putTextRect(img, f'{obj["class"]} {obj["confidence"]}', (max(0, x1), max(35, y1)), scale=0.7, thickness=1)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# classNames = []
# with open('/home/rashmihk/class_name.csv', 'r') as class_file:
#     reader = csv.reader(class_file)
#     for row in reader:
#         classNames.append(row)
classNames = ["Dolo 650", "Saridon"]
# classNames = ["Cetirizin Hydrochloride", "Cetirizine all day allergy relief", "Cetirizine Care", "Cetirizine HCL 10MG", "Cetirizine mYLAN pHARMA 10mg", "Cetfull 10mg", "IBUPROFEN 400mg", "Cetirizine IRIZINE 10", "Cetirizine", "cetrasyl 10", "IBUPROFEN 200mg", "Ibuprofen BRUFEN 400", "Hydrochloride 10mg", "Cetirizine Hydrochloride Film Coated 10mg", "BRUFEN 600", "ibuprofen 200mg", "Hiscold-cz", "Cetirizine Tablet IP", "Cetirizine HCL", "Cetirizine Medication", "Major Cetirizine", "Cetirizine Benadryl One", "Lifcet", "Cetirizine STADA 10 MG", "Cetirizine 5mg", "Okacet 10mg", "allacon", "PIRACIT", "Benadryl Allergy", "Benadryl Diphenhydramine HCL 25mg", "BenadrylEXTRA STRENGTH", "Benadryl Allergy RELIFE", "Benadryl Total", "Benadryl ALLERGY PARA ALERGIAS", "Benadryl Allergy ONE A DAY", "Benadryl Allergy PLUS", "Benadryl ALLERGY CHEWABLES", "Benadryl ALLERGY LIQUID RELEASE", "Benadryl PLUS CAPSULES", "Benadryl Allergy RELIEF PLUS", "Benadryl DR cough lozenges", "Benadryl ALLERGY FASTMELT", "Allergy Relief", "Benadryl Allergy Relief Acrivastine", "Benadryl Gel", "Banophin HCL 50mg", "Benadryl Chewable", "Comzyall Plus", "Benadryl tablet", "children's Benadryl", "Crocin 120", "Crocin 650", "D\"cold Total", "Crocin", "Crocin cold & flu tablet", "Crocin Advance", "Crocin Pain Relief", "Crocin Drops", "Crocin Cold n\" Flu", "Modlip ASG 20", "Modlip ASG 75", "Febrex", "Leemol-500", "Flumol-650", "Pacimol 650", "Pacimol 500", "Fepanil", "Fepanil 500", "Fepanil 650", "Paracip 650", "Paracip 500", "Paracip", "Naprosyn 500", "Naprosyn SR", "Naprosyn 500+", "Naprosyn", "Ultramol 650", "Naprosyn 250+", "Calpol650", "Ultramol 500", "Calpol 500", "Dolopar 650", "Dolopar", "Paragreat 650", "P-250", "P-750", "Macfast 500", "XTPARA 650", "XTPARA 1000", "XTPARA proglet", "JWARSHOONYA", "Koflet", "Tempros-KID", "Tempros-300", "Tempros-500", "Tempros-650", "Leemol-650", "Amidol-RB", "Amidol-300", "Amidol-650", "Ifimol 650", "Ifimol 500", "Ifimol 4c", "Ifimol 3c", "Idamol 500", "Dolo 500", "Dolo 650", "Disprin"]
# classNames = ['Modlip ASG 20', 'Modlip ASG 75', 'Febrex', 'Leemol-500', 'Flumol-650', 'Pacimol 650', 'Pacimol 500', 'Fepanil', 'Fepanil 500', 'Fepanil 650', 'Paracip 650', 'Paracip 500', 'Paracip', 'Naprosyn 500', 'Naprosyn SR', 'Naprosyn 500+', 'Naprosyn', 'Ultramol 650', 'Naprosyn 250+', 'Calpol650', 'Ultramol 500', 'Calpol 500', 'Dolopar 650', 'Dolopar', 'Paragreat 650', 'P-250', 'P-750', 'Macfast 500', 'XTPARA 650', 'XTPARA 1000', 'XTPARA proglet', 'JWARSHOONYA', 'Koflet', 'Tempros-KID', 'Tempros-300', 'Tempros-500', 'Tempros-650', 'Leemol-650', 'Amidol-RB', 'Amidol-300', 'Amidol-650', 'Ifimol 650', 'Ifimol 500', 'Ifimol 4c', 'Ifimol 3c', 'Idamol 500', 'Dolo 500', 'Dolo 650', 'Disprin']
# classNames = ["Dolo650", "paracetomol500", "paracetomol650", "paracetomoeasy", "paracip500", "para500", "paradolo 650" , "raj para"]  # Add or modify the class names as needed
detect_objects(classNames)
