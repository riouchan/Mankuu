DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'DEV_ManqooMaster',  # Your database name
        'USER': 'tgergi',  # Your database username
        'PASSWORD': 'Qertgaer32',  # Your database password
        'HOST': 'rtydfrhytc.database.windows.net',  # Your database host
        # Your database port (if needed, otherwise leave as empty string)
        'PORT': '2425',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;',
        },
    }
}
