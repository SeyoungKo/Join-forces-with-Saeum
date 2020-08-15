package com.conference.assistant.springboot.conferenceassistantspringboot.domain.team;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Status {
    INVALID("STATUS_INVALID", "삭제된팀"),
    VALID("STATUS_VALID", "유효한팀");

    private final String key;
    private final String title;
}
