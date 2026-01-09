# HATEOAS Implementation with Flask-Marshmallow

## ✅ Completed Implementation

This project demonstrates a complete HATEOAS (Hypertext as the Engine of Application State) implementation using Flask and Marshmallow.

## What Was Done

### 1. **Installed Dependencies**
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- All required Flask extensions

### 2. **Configured Marshmallow Schema**
Created `NewsletterSchema` with:
- Auto-generated fields (title, published_at)
- HATEOAS hyperlinks (self, collection)
- Single and multiple record schemas

### 3. **Updated All API Endpoints**
Replaced `to_dict()` with `schema.dump()` in:
- `GET /newsletters` - List all newsletters
- `POST /newsletters` - Create newsletter
- `GET /newsletters/<id>` - Get single newsletter
- `PATCH /newsletters/<id>` - Update newsletter
- `DELETE /newsletters/<id>` - Delete newsletter

### 4. **Database Setup**
- Ran migrations: `flask db upgrade`
- Seeded database: `python seed.py`

## API Response Format

Each resource now includes HATEOAS links:

```json
{
  "title": "Newsletter Title",
  "published_at": "2026-01-09T12:26:28",
  "url": {
    "self": "/newsletters/1",
    "collection": "/newsletters"
  }
}
```

## Testing

Run the test script:
```bash
python test_hateoas.py
```

Start the server:
```bash
cd server
python app.py
```

Test endpoints:
```bash
curl http://localhost:5555/newsletters
curl http://localhost:5555/newsletters/1
```

## Key Benefits

✓ **Stateless Navigation** - URLs guide users to related resources
✓ **Self-Documenting API** - Each response shows available actions
✓ **RESTful Compliance** - Follows REST architectural constraints
✓ **Client Independence** - Clients don't need hardcoded URLs
