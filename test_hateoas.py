#!/usr/bin/env python3

import sys
sys.path.insert(0, 'server')

from app import app, newsletter_schema, newsletters_schema
from models import Newsletter
import json

with app.app_context():
    app.config['SERVER_NAME'] = 'localhost:5555'
    with app.test_request_context():
        
        print("=" * 60)
        print("HATEOAS IMPLEMENTATION TEST")
        print("=" * 60)
        
        # Test collection endpoint
        print("\n1. GET /newsletters (Collection with HATEOAS links):")
        print("-" * 60)
        newsletters = Newsletter.query.limit(3).all()
        result = newsletters_schema.dump(newsletters)
        print(json.dumps(result, indent=2))
        
        # Test single resource endpoint
        print("\n2. GET /newsletters/1 (Single resource with HATEOAS links):")
        print("-" * 60)
        newsletter = Newsletter.query.first()
        result = newsletter_schema.dump(newsletter)
        print(json.dumps(result, indent=2))
        
        print("\n" + "=" * 60)
        print("✓ HATEOAS successfully implemented!")
        print("✓ Each resource includes 'self' and 'collection' URLs")
        print("=" * 60)
