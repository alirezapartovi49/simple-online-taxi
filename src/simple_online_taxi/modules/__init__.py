from pathlib import Path
from importlib import import_module
import sys
import logging
from os.path import dirname, abspath


logger = logging.getLogger("uvicorn.error")

SRC_DIR = dirname(dirname(dirname(abspath(__file__))))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
    logger.info(f"Added to sys.path: {SRC_DIR}")

def register_models():
    base_path = Path(__file__).parent
    logger.info(f"Scanning for models in: {base_path}")

    found_any = False

    for module_dir in base_path.iterdir():
        if not module_dir.is_dir():
            continue

        module_name = f"src.simple_online_taxi.modules.{module_dir.name}"
        logger.debug(f"Checking module: {module_name}")

        if (module_dir / "models.py").exists():
            models_module = f"{module_name}.models"
            try:
                import_module(models_module)
                logger.info(f"Successfully imported: {models_module}")
                found_any = True
            except ImportError as e:
                logger.error(f"Failed to import {models_module}: {str(e)}")
                continue

        # Check for models/ directory
        elif (module_dir / "models").is_dir():
            models_dir = module_dir / "models"
            logger.debug(f"Found models directory: {models_dir}")

            for model_file in models_dir.iterdir():
                if (model_file.suffix == '.py' and
                    not model_file.stem.startswith('__')):

                    model_module = f"{module_name}.models.{model_file.stem}"
                    try:
                        import_module(model_module)
                        logger.info(f"Successfully imported: {model_module}")
                        found_any = True
                    except ImportError as e:
                        logger.error(f"Failed to import {model_module}: {str(e)}")

    if not found_any:
        logger.warning("No model files found in any modules")
    else:
        logger.info("Completed model registration")
