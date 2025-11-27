def processar_dados_sensor(cultura, umidade, ph, temperatura, nutrientes):
    """
    Esta função atua como um 'Agrônomo Digital'.
    Ela analisa os dados brutos e retorna alertas e recomendações.
    """
    msgs_alerta = []
    msgs_acao = []

    # --- REGRA 1: ANÁLISE DE UMIDADE ---
    if cultura == 'Soja':
        # Soja gosta de 60-70%
        if umidade < 50:
            msgs_alerta.append("⚠️ Umidade Baixa (Risco Hídrico)")
            msgs_acao.append(
                "Sugestão: Ativar irrigação por gotejamento (aumentar 20mm).")
        elif umidade > 85:
            msgs_alerta.append("⚠️ Solo Encharcado")
            msgs_acao.append(
                "Sugestão: Drenar solo ou suspender irrigação imediatamente.")

    elif cultura == 'Acai':
        # Açaí ama água (região amazônica), ideal > 80%
        if umidade < 70:
            msgs_alerta.append("🔴 URGENTE: Umidade Crítica para Açaí")
            msgs_acao.append(
                "Sugestão: Irrigação pesada necessária imediatamente.")

    # --- REGRA 2: ANÁLISE DE pH ---
    # pH ideal geral costuma ser entre 6.0 e 6.5
    if ph < 5.5:
        msgs_alerta.append("⚠️ Solo Ácido")
        msgs_acao.append("Sugestão: Aplicar calagem (Calcário) para correção.")
    elif ph > 7.5:
        msgs_alerta.append("⚠️ Solo Alcalino")
        msgs_acao.append(
            "Sugestão: Avaliar aplicação de gesso ou fertilizantes acidificantes.")

    # --- REGRA 3: TEMPERATURA E NUTRIENTES ---
    if temperatura > 35:
        msgs_alerta.append("🔥 Estresse Térmico Alto")
        # Não há muito o que fazer sobre o sol, mas avisa o gestor

    if nutrientes < 4:
        msgs_alerta.append("⚠️ Deficiência Nutricional Detectada")
        msgs_acao.append("Sugestão: Programar adubação NPK na próxima janela.")

    # Se estiver tudo certo
    if not msgs_alerta:
        msgs_alerta.append("✅ Condições Ideais")
        msgs_acao.append("Manter monitoramento padrão.")

    return msgs_alerta, msgs_acao
