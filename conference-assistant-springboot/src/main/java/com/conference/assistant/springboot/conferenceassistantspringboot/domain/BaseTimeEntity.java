package com.conference.assistant.springboot.conferenceassistantspringboot.domain;

import lombok.Getter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.EntityListeners;
import javax.persistence.MappedSuperclass;
import java.time.LocalDateTime;

@Getter
@MappedSuperclass // entity들의 createdDate, modifiedDate를 자동으로 관리
@EntityListeners(AuditingEntityListener.class) // Auditing
public class BaseTimeEntity {

    @CreatedDate
    private LocalDateTime createdDate; // createdDate

    @LastModifiedDate
    private LocalDateTime modifiedDate; // modifiedDate
}
