from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES = [
    {
        'id':
        1,
        'title':
        'SmartConnect IoT Solutions',
        'price':
        'Php 20 000.00',
        'description':
        "GalosTech's SmartConnect IoT solutions redefine connectivity. Immerse your business in the era of intelligent networks, where devices communicate seamlessly for optimized operations. Our bespoke IoT services cater to diverse industries, offering unparalleled connectivity, data analytics, and remote monitoring capabilities."
    },
    {
        'id':
        2,
        'title':
        'Visionary Insights with GalosVision',
        'price':
        'Php 30 000.00',
        'description':
        "GalosVision, our revolutionary Computer Vision service, grants your business the gift of sight. Empower your systems to interpret visual data, from facial recognition in security systems to defect identification in manufacturing. GalosVision is your window to actionable insights derived from the visual world, transforming the way you perceive and understand your environment."
    },
    {
        'id':
        3,
        'title':
        'IntelligentML Solutions',
        'price':
        'Php 30 000.00',
        'description':
        "Elevate your organization with the power of IntelligentML by GalosTech. Our Machine Learning solutions adapt and evolve, enabling your business to predict trends, optimize processes, and make data-driven decisions. From personalized customer experiences to predictive maintenance in industrial settings, GalosTech's IntelligentML solutions revolutionize how you harness the potential of data."
    },
]


@app.route("/")
def hello_world():
  return render_template("home.html", services=SERVICES)


@app.route("/api/services")
def list_services():
  return jsonify(SERVICES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
