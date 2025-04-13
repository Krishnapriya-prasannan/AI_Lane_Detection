import cv2
import numpy as np

def canny_edge_detector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[
        (100, height),
        (image.shape[1] - 100, height),
        (image.shape[1] // 2 + 50, height // 2 + 50),
        (image.shape[1] // 2 - 50, height // 2 + 50),
    ]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return line_image

def main():
    cap = cv2.VideoCapture("test_video.mp4")  # Replace with your video file

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        canny = canny_edge_detector(frame)
        roi = region_of_interest(canny)
        lines = cv2.HoughLinesP(roi, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=50)
        line_image = display_lines(frame, lines)
        combo = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

        cv2.imshow("Lane Detection", combo)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
