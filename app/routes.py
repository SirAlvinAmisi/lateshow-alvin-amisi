from flask import Blueprint, request, jsonify
from .models import Episode, Guest, Appearance
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return {'message': 'Welcome to the Late Show API!'}

@main.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [a.to_dict() for a in episode.appearances]
    })

@main.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])

@main.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        rating = int(data['rating'])
        episode_id = int(data['episode_id'])
        guest_id = int(data['guest_id'])

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return jsonify({"errors": ["Invalid episode or guest ID"]}), 400

        appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
