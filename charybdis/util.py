import os

from flask_sqlalchemy import SQLAlchemy

from .app.config import Config


def is_first_start() -> bool:
    return not os.path.exists(os.path.join(Config.APP_DIR, "charybdis.lock"))


def first_start(db: SQLAlchemy) -> None:
    db.create_all()
    db.session.commit()

    DEFAULT_INSERTS = """INSERT INTO public.domain (created_at, updated_at, slug, name, description, uuid, is_active, id)
                             VALUES ('2019-10-01 10:18:19.842186', null, 'global', 'Global', '', '00000000-0000-0000-0000-000000000000', null, 1);

                        INSERT INTO public.user_role (created_at, updated_at, slug, id)
                            VALUES ('2019-10-01 10:18:33.406989', null, 'admin', 1);
                        
                        INSERT INTO public.user_role (created_at, updated_at, slug, id)
                            VALUES ('2019-10-01 10:18:33.406989', null, 'reader', 2);
                        
                        INSERT INTO public.user_role (created_at, updated_at, slug, id)
                            VALUES ('2019-10-01 10:18:33.406989', null, 'moderator', 3);

                        INSERT INTO public."user" (created_at, updated_at, first_name, last_name, patronymic, birthday, role_id, is_active, username, password_hash, uuid, domain_id, id)
                            VALUES ('2019-10-01 10:19:13.283768', null, '1', '1', null, '2019-10-29', 1, true, 'basic',
                            '$pbkdf2-sha512$25000$D.G8t/beGwOgdM4ZY8y5Vw$WsKIhGgwUyhEOp5LAaU/MQFTIQeD3Hzil5Lzuys95iKwhLOYdFw8WPt.BAASS9bTIPRIzebfMe3pRieDzbFCnQ', '00000000-0000-0000-0000-000000000000', 1, 2);"""

    db.engine.execute(DEFAULT_INSERTS)
    db.session.commit()

    with open(os.path.join(Config.APP_DIR, "charybdis.lock"), "w") as f:
        f.write("1")
