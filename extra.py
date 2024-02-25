"""
            INSERT INTO clerk_users (user_id, first_name, last_name, email, gender, created_at, updated_at, last_sign_in_at, phone_numbers, username)
            SELECT * FROM clerk_users;
            
            INSERT INTO clerk_organizations (organization_id, name, slug, created_at, updated_at, created_by)
            SELECT * FROM clerk_organizations;
            
            INSERT INTO clerk_organization_memberships (user_id, organization_id, role)
            SELECT * FROM clerk_organization_memberships;
        """