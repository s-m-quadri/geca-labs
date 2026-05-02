USE clinic_db;

-- Populate Specializations first (Parent Table)
INSERT INTO specializations (spec_name) VALUES
  ('Cardiology'),
  ('Neurology'),
  ('Pediatrics'),
  ('Orthopedics');

-- Populate Doctors (Child Table)
-- We use the IDs 1, 2, 3, 4 which were generated above
INSERT INTO doctors (doc_name, spec_id) VALUES
  ('Dr. Alice Smith', 1),
  ('Dr. Brian Wong', 1),
  ('Dr. Catherine Reed', 2),
  ('Dr. David Gupta', 3),
  ('Dr. Elena Martinez', 4);